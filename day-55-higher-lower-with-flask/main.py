from flask import Flask
app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"

    return wrapper


def make_underline(function):
    def wrapper():
        return f"<u>{function()}</u>"

    return wrapper


def make_emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"

    return wrapper


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">This is Home page, written by h1 tag of HTML</h1>' \
           '<p>and this is just aфывфывф simple paragraph</p>' \



@app.route("/bye")
@make_underline
@make_bold
@make_emphasis
def say_bye():
    return "Bye!"


@app.route("/username/<path:name>/<int:number>")
def greet(name, number):
    return f"Hello there {name} and number is {number}"


if __name__ == "__main__":
    app.run(debug=False)
