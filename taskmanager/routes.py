from flask import render_template, request, redirect, url_for, flash
from taskmanager import app, db
from taskmanager.models import User, Movie
from werkzeug.security import generate_password_hash
app.app_context().push()

@app.route("/")
def home():
    return render_template("base.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/movies")
def movies():
    movies = list(Movie.query.order_by(Movie.movie_title).all())
    return render_template("movies.html", movies=movies)



@app.route("/add_movie", methods=["GET", "POST"])
def add_movie():
    movies = list(Movie.query.order_by(Movie.movie_title).all())
    if request.method == "POST":
        movie = Movie(
            movie_title=request.form.get("movie_title"),
            movie_description=request.form.get("movie_description"),
            movie_year=request.form.get("movie_year"),
            movie_genre=request.form.get("movie_genre")
        )
        db.session.add(movie)
        db.session.commit()
        return redirect(url_for("movies"))
    return render_template("add_movie.html", movies=movies)



@app.route("/edit_movie/<int:movie_id>", methods=["GET", "POST"])
def edit_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    movies = list(Movie.query.order_by(Movie.movie_title).all())
    if request.method == "POST":
            movie.movie_title=request.form.get("movie_title"),
            movie.movie_description=request.form.get("movie_description"),
            movie.movie_year=request.form.get("movie_year"),
            movie.movie_genre=request.form.get("movie_genre"),
            
            db.session.commit()
            return redirect(url_for("movies"))
    return render_template("edit_movie.html", movie=movie,)


@app.route("/delete_movie/<int:movie_id>")
def delete_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("movies"))


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("e_mail")
        message = request.form.get("message")

        
        flash(f"Thanks {name}, we received your message!", "success")
        return redirect(url_for("contact"))  
    return render_template("contact.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        # check if username already exists in db
        existing_user = User.query.filter(User.username == request.form.get("username").lower()).all()

        if existing_user:
            flash("Username already exists", "error")
            return redirect(url_for("register"))

        if request.form.get("password") != request.form.get("confirm_password"):
            # Checks if the password match
            flash("Passwords do not match!", "error")
            return redirect(url_for("register"))

        # adds a new user to DB
        user = User(
            username=request.form.get("username").lower(),
            password=generate_password_hash(request.form.get("password"))
            )
        db.session.add(user)
        db.session.commit()


        session["user"] = request.form.get("username").lower()
        flash("You have successfully registered!", "success")
        return render_template("profile.html", username=session["user"])

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    
    if request.method == "POST":
        # Checks if the username alrady exists
        existing_user = \
         User.query.filter(User.username ==
                            request.form.get("username").lower()).all()

        if existing_user:
            if check_password_hash(existing_user[0].password,
                                   request.form.get("password")):
                # Checks if the username and the password match
                session["user"] = request.form.get("username").lower()
                flash("Click on your username to load profile")
                return render_template("profile.html",
                                       username=session["user"])
            else:
                # Informs user they have input the wrong data
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            # Informs user they have input the wrong data
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")

        