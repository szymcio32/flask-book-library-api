from flask import Blueprint

errors_bp = Blueprint('errors', __name__)

from book_library_app.errors import errors