from flask import Flask
import random
random_num = random.randint(0, 9)
print(random_num)
app = Flask(__name__)


@app.route("/")
def higher_lower():
    return '<h1>Guess a number between 0 and 9</h1>\
    <img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExeXUydzV3aG4wbnM0Zmdmbjk0MHduaTNkeXF5eDJ5OHo0Y2hhOXdwcSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/c7PcKQlOqZ8Ws/giphy.gif">'


@app.route("/<int:number>")
def guess(number):
    if number > random_num:
        return "<h1 style='color: red'>Too High, try again!</h1>"\
               "<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMzVwanJnbGd0bnBtaHl3d3FrMmZteXpyaXAwazc4d3JtcmR4YTg3cSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/fvpsznYW7rFTk9eSww/giphy.gif'>"
    elif number < random_num:
        return "<h1 style='color: blue'>Too Low, try again!</h1>""<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExbnJlejA3a3JnMGphMTFuYXl0a21mbzU0ZjUzenpyaHJqYm81ejM0ZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/TgmiJ4AZ3HSiIqpOj6/giphy.gif'>"
    else:
        return "<h1 style='color: green'>You found the number!</h1>""<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZjB3YjVvOXVlMmN2cnVqNHkzN215aWtsY3FzZHg0ZXY3dDkyaHFmYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/tHIRLHtNwxpjIFqPdV/giphy.gif'>"


