from flask import Blueprint

bp = Blueprint('genders',
               __name__,
               template_folder="templates",
               url_prefix="/genders")

