from flask import Flask
from flask import render_template
import requests
from posts import Post

app = Flask(__name__)
URL = "https://api.npoint.io/998f66f97685dbd14659"

post_objs = []
post = requests.get(url=URL).json()

for items in post:
    post_obj = Post(items["id"], items["title"], items["author"], items["date"], items["summary"], items["body"], items["image_url"])
    post_objs.append(post_obj)


@app.route("/")
def home():
    return render_template("index.html", all_posts=post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/<int:index>")
def show_post(index):
    requested_post = None
    for item in post_objs:
        if item.id == index:
            requested_post = item
    return render_template("post.html", post=requested_post)
