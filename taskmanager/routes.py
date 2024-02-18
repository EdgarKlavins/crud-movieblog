from flask import render_template, request, redirect, url_for, flash, session
from taskmanager import app
from taskmanager.models import User, Movie
from taskmanager import db
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from sqlalchemy import desc

app.app_context().push()

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    """
    Brings user to index page
    """
    return render_template("about.html")


@app.route("/index")
def index():
    """
    Brings user to index page
    """
    all_movies = Movie.query.all()
    return render_template("index.html", all_movies=all_movies)


@app.route("/movies")
def movies():
    """
    Function checks if user has been logged in session and allows to browse  movies

    """
    if "user" not in session:
        
        flash("You need to log in to access this page.", "error")
        return redirect(url_for("login"))
    movies = list(Movie.query.order_by(desc(Movie.id)).all())
    return render_template("movies.html", movies=movies)



@app.route("/add_movie", methods=["GET", "POST"])
def add_movie():
    """
    Function checks if user has been logged in session and allows to add movie

    """
    if request.method == "POST":
        
        user_id = session.get("user_id")

        
        if user_id is None:
            flash("You need to log in to add a movie.", "error")
            return redirect(url_for("login"))

        
        movie = Movie(
            movie_title=request.form.get("movie_title"),
            movie_description=request.form.get("movie_description"),
            movie_year=request.form.get("movie_year"),
            movie_genre=request.form.get("movie_genre"),
            user_id=user_id  
        )

        db.session.add(movie)
        db.session.commit()

        flash("Movie added successfully.", "success")
        return redirect(url_for("movies"))

    return render_template("add_movie.html", movies=movies)



@app.route("/edit_movie/<int:movie_id>", methods=["GET", "POST"])
def edit_movie(movie_id):
    """
    Function checks if user id matches session id and allows to edit movie
    """
    movie = Movie.query.get_or_404(movie_id)

    print("Session user_id:", session.get("user_id"))
    print("Movie user_id:", movie.user_id)
    
    if "user_id" not in session or movie.user_id != session["user_id"]:
        
        flash("You do not have permission to edit this movie.", "error")
        return redirect(url_for("movies"))

    if request.method == "POST":
        movie.movie_title = request.form.get("movie_title")
        movie.movie_description = request.form.get("movie_description")
        movie.movie_year = request.form.get("movie_year")
        movie.movie_genre = request.form.get("movie_genre")
        
        db.session.commit()
        return redirect(url_for("movies"))

    return render_template("edit_movie.html", movie=movie)


@app.route("/delete_movie/<int:movie_id>")
def delete_movie(movie_id):
    """
    Function checks if user id matches session id and allows to delete movie
    """
    movie = Movie.query.get_or_404(movie_id)
    if "user_id" not in session or movie.user_id != session["user_id"]:
        
        flash("You do not have permission to delete this movie.", "error")
        return redirect(url_for("movies"))

    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("movies"))


@app.route("/contact", methods=["GET", "POST"])
def contact():
    """
    Function  that checks if contact page is submitted and flashes message
    """
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("e_mail")
        message = request.form.get("message")

        
        flash(f"Thanks {name}, we received your message!", "success")
        return redirect(url_for("contact"))  
    return render_template("contact.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Function that creates new account and checks if username is not takken.
    """
    if request.method == 'POST':
        
        existing_user = User.query.filter(User.username == request.form.get("username").lower()).all()

        if existing_user:
            flash("Username already exists", "error")
            return redirect(url_for("register"))

        if request.form.get("password") != request.form.get("confirm_password"):
            
            flash("Passwords do not match!", "error")
            return redirect(url_for("register"))

        
        user = User(
            username=request.form.get("username").lower(),
            password=generate_password_hash(request.form.get("password"))
            )
        db.session.add(user)
        db.session.commit()


        
        flash("You have successfully registered!", "success")
        return render_template("login.html")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Function that that checks username and password
    
    """
    
    if request.method == "POST":
        
        existing_user = \
         User.query.filter(User.username ==
                            request.form.get("username").lower()).all()

        if existing_user:
            if check_password_hash(existing_user[0].password,
                                   request.form.get("password")):
                
                session["user"] = request.form.get("username").lower()
                session["user_id"] = existing_user[0].id 
                flash("Welcome!")
                return redirect(url_for("index", username=session["user"]))
            else:
                
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    A function that displays the user's name
    and movies they have created
    """
    movies = list(Movie.query.order_by(Movie.movie_title).all())
    
    if "user" in session:
        """
        Checks if the user is logged in.
        """
        return render_template("profile.html", username=session["user"],
                               movies=movies,)
    else:
        return redirect(url_for("login"))



@app.route("/logout")
def logout():
    """
    Clears all session data to log out user
    """
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("index"))