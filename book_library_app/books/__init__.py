from flask import Blueprint

books_bp = Blueprint('books', __name__)

from book_library_app.books import books