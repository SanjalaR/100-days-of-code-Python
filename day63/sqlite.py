# import sqlite3
#
# db = sqlite3.connect('books-collection.db')
# cursor = db.cursor()
# cursor.execute('CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) '
#                'NOT NULL, rating FLOAT NOT NULL)')
# cursor.execute('INSERT INTO books VALUES (1, "HP", "JKR", 9.3)')
# db.commit()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


class Base(DeclarativeBase):
    pass


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    author: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[float] = mapped_column(nullable=False)


with app.app_context():
    db.create_all()


# Create
with app.app_context():
    new_book = Book(id=1, title='HP', author='JKR', rating=9.3)
    db.session.add(new_book)
    db.session.commit()


# Read all records
with app.app_context():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalar()


# Read particular record
with app.app_context():
    book = db.session.execute(db.select(Book).where(Book.title == 'HP')).scalar()


# Update
with app.app_context():
    book = db.session.execute(db.select(Book).where(Book.title == 'HP')).scalar()
    # or book = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    # or book = db.get_or_404(Book, book_id)
    book.title='HP and the Chamber of Secrets'
    db.session.commit()

# Delete
with app.app_context():
    book = db.session.execute(db.select(Book).where(Book.id == 1)).scalar()
    db.session.delete(book)
    db.session.commit()


