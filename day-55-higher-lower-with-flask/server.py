from random import randint
from flask import Flask

app = Flask(__name__)

answer = randint(1, 10)

win_url = "https://media2.giphy.com/media/GeimqsH0TLDt4tScGw/giphy.gif"
lower_url = "https://c.tenor.com/RH9jOdC3R80AAAAd/cat-bop.gif"
higher_url = "https://c.tenor.com/JckJNSfq3ngAAAAd/cat-meme.gif"


@app.route('/')
def hello_world():
    return f'<h1>Guess the number between 1 and 10!</h1>' \
           f'<img src="https://media.giphy.com/media/LMn7PRCVDcnvO/giphy.gif"' \
           f'<br><h2>Add it into link!</h2>' \



def too_high():
    return "<h1>Your answer is lower!</h1>" \
           f"<img src={lower_url}>"


def too_low():
    return "<h1>Your answer is higher!</h1>" \
           f"<img src={higher_url}"


@app.route('/<int:number>')
def enter_number(number):
    if number > answer:
        return too_high()
    elif number < answer:
        return too_low()
    else:
        return "correct!"


if __name__ == "__main__":
    app.run(debug=True)
