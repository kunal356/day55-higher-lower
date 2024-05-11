from flask import Flask
from random import randint
random_num = randint(0, 10)
print(random_num)
app = Flask(__name__)


@app.route("/")
def home():
    return "<h1> Guess a number between 0 and 9</h1>"\
        "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' alt='guess-img'>"


@app.route("/<int:num>")
def guess(num):
    if num < random_num:
        return "<h1 color='red'> Too low, try again!</h1>"\
            "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' alt='low-img'>"
    elif num > random_num:
        return "<h1 color='purple'> Too high, try again!</h1>"\
            "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' alt='high-img'>"
    else:
        return "<h1 color='green'>You found me!</h1>"\
            "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' alt='correct-img'>"


if __name__ == "__main__":
    app.run(debug=True)
