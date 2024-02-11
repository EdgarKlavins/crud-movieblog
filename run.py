import os
from flask import Flask, render_template, request, flash, redirect, url_for
from wtforms import StringField, TextAreaField, SubmitField, validators
from wtforms.validators import InputRequired, Email
from flask_wtf import FlaskForm
from taskmanager import app




if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )