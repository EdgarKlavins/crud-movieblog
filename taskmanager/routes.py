from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import User, Movie, Genre, Year, Description
app.app_context().push()

@app.route("/")
def home():
    return render_template("base.html")


@app.route("/movies")
def movies():
    return render_template("movies.html")


@app.route("/add_movie", methods=["GET", "POST"])
def add_movie():
    if request.method == "POST":
        movie = Movie(movie_name=request.form.get("movie_name"))
        db.session.add(movie)
        db.session.commit()
        return redirect(url_for("movies"))
    return render_template("add_movie.html")