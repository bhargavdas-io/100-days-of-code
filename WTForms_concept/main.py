from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, Form
from wtforms import validators
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.secret_key = "thisisasecretkey"


class MyForm(FlaskForm):
    email = StringField(label='email', validators=[validators.DataRequired(), validators.Email()])
    password = PasswordField(label='password', validators=[validators.DataRequired(), validators.Length(min=8)])
    submit = SubmitField(label='submit')


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = MyForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", my_form=login_form)