from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def form():
    return render_template('index.html')


@app.route("/login", methods=['POST'])
def received():
    username = request.form["username"]
    password = request.form["password"]
    return f"<h1> {username}, {password} </h1>"
