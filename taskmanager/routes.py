from flask import render_template, request, redirect, url_for, flash
from taskmanager import app, db
from taskmanager.models import User, Movie
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