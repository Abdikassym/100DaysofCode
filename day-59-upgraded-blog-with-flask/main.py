from flask import Flask, render_template
import requests

app = Flask(__name__)

posts_endpoint = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(posts_endpoint).json()


@app.route('/')
def hello():
    return render_template('index.html', posts=response)


@app.route('/about')
def get_about():
    return render_template('about.html')


@app.route('/contact')
def get_contact():
    return render_template('contact.html')


@app.route('/post_<int:num>')
def get_post(num):
    return render_template("post.html", info=response[int(num) - 1])


if __name__ == "__main__":
    app.run(debug=True)
