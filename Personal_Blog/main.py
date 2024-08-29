import os
import smtplib

from dotenv import load_dotenv
from flask import Flask, render_template, request
import requests
from posts import Post

load_dotenv()
SENDER = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]
RECEIVER = os.environ["TO"]

URL = "https://api.npoint.io/998f66f97685dbd14659"
app = Flask(__name__)

post_objs = []
post = requests.get(url=URL).json()

for items in post:
    post_obj = Post(items["id"], items["title"], items["author"], items["date"], items["summary"], items["body"],
                    items["image_url"])
    post_objs.append(post_obj)


@app.route("/")
def home():
    return render_template("index.html", all_posts=post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        mail(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


@app.route("/<int:index>")
def show_post(index):
    requested_post = None
    for item in post_objs:
        if item.id == index:
            requested_post = item
    return render_template("post.html", post=requested_post)


def mail(name, email, phone, message):
    email_msg = f"Subject: New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(SENDER, PASSWORD)
        connection.sendmail(from_addr=SENDER, to_addrs=RECEIVER, msg=email_msg)
