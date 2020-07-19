from flask import Blueprint

auth_bp = Blueprint('auth', __name__)

from book_library_app.auth import auth