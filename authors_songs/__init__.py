from flask import Blueprint

bp = Blueprint('authors_songs',
               __name__,
               template_folder="templates",
               url_prefix="/authors_songs")
