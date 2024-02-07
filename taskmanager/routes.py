from flask import render_template
from taskmanager import app, db
from taskmanager.models import User, Movie, Genre, Year, Description
app.app_context().push()

@app.route("/")
def home():
    return render_template("base.html")
    