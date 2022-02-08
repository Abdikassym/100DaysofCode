import datetime
from flask import Flask, render_template
import random
import requests

app = Flask(__name__)


@app.route('/')
def home():
    current_year = datetime.datetime.now().year
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, current_year=current_year)


@app.route("/guess/<name>")
def guess(name):
    age_endpoint = f"https://api.agify.io?name={name}"
    gender_endpoint = f"https://api.genderize.io/?name={name}"

    age_response = requests.get(age_endpoint).json()
    gender_response = requests.get(gender_endpoint).json()

    gender = gender_response["gender"]
    age = age_response["age"]

    gender_prob = gender_response["probability"]
    name_count = age_response["count"]
    return render_template("guess.html", cap_name=name.capitalize(), gender=gender, age=age, name_count=name_count,
                           gender_prob=gender_prob)


@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
