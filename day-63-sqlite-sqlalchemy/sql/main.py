from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=0)
    author = db.Column(db.String(120), unique=False, nullable=0)
    rating = db.Column(db.Float, nullable=0)

    def __repr__(self):
        return f"<book {self.title}>"


db.create_all()


# hp = Book(title="It", author="Stephen King", rating=9)
# db.session.add(hp)
# db.session.commit()

all_books = Book.query.all()


def get_books():
    for book in all_books:
        print(
            book.id,
            book.title,
            book.author,
            book.rating
        )

get_books()

it_book = Book.query.filter_by(title="It").first()
print(it_book.author)

book_to_update = Book.query.filter_by(title="Harry Potter And The Philosopher's Stone").first()
book_to_update.title = "Harry Potter And The Deathly Hallows"
db.session.commit()
print("Successful change by title!")

get_books()

second_upgrade = Book.query.get(3)
second_upgrade.title = "4th Wave"
db.session.commit()
print("Successful change by id!")

get_books()

book_to_delete = Book.query.get(3)
db.session.delete(book_to_delete)
db.session.commit()

get_books()
