from flask import Flask

app = Flask(__name__)


def make_bold(func):
    def wrap(*args, **kwargs):
        return '<b>' + func(*args, **kwargs) + '</b>'

    return wrap


def make_italic(func):
    def wrap(*args, **kwargs):
        return '<em>' + func(*args, **kwargs) + '</em>'

    return wrap


def underline(func):
    def wrap(*args, **kwargs):
        return '<u>' + func(*args, **kwargs) + '</u>'

    return wrap


@app.route("/")
@make_bold
@make_italic
@underline
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/<username>/<int:age>")  # Get input from user in URL <xyz>. Default is string.
def name(username, age):
    return f"Hello {username}, you are {age} years old."
