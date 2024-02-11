import os
from flask import Flask, render_template, request, flash, redirect, url_for
from wtforms import StringField, TextAreaField, SubmitField, validators
from wtforms.validators import InputRequired, Email
from flask_wtf import FlaskForm
from taskmanager import app






class ContactForm(FlaskForm):
    name = StringField('Name', [validators.InputRequired()])
    email = StringField('Email', [validators.InputRequired(), validators.Email()])
    message = TextAreaField('Message', [validators.InputRequired()])
    submit = SubmitField('Submit')


    # Adding confirmation to the user that form was sent.
@app.route("/contact", methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        print(f"Name: {name}\nEmail: {email}\nMessage: {message}")
        flash(f"We received your email, thanks {name}!", 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html', form=form)



if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )