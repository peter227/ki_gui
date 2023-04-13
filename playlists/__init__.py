from flask import Blueprint

bp = Blueprint('playlists',
               __name__,
               template_folder="templates",
               url_prefix="/playlists")
