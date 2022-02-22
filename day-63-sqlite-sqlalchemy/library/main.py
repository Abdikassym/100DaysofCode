from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///library.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=False, nullable=0)
    author = db.Column(db.String(80), unique=False, nullable=0)
    rating = db.Column(db.Float, nullable=0)

    def __repr__(self):
        return f"<book {self.title}>"


db.create_all()


@app.route('/')
def home():
    all_books = Book.query.all()
    return render_template('index.html', book_list=all_books, book_list_len=len(all_books))


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        book_name = request.form["book_name"]
        book_author = request.form["book_author"]
        book_rating = request.form["book_rating"]

        book = Book(title=book_name, author=book_author, rating=book_rating)
        db.session.add(book)
        db.session.commit()

        return redirect("/")
    return render_template('add.html')


@app.route('/edit<num>', methods=["POST", "GET"])
def edit_rating(num):
    current_book = Book.query.get(num)
    print(type(current_book.rating))
    if request.method == "POST":
        print(request.form["new_rating"])
        current_book.rating = request.form["new_rating"]
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('edit.html', book=current_book)


@app.route('/delete')
def delete_book():
    book_to_delete = Book.query.get(request.args["num"])
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

