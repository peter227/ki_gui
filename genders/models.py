from db import db


class Genders(db.Model):
    id_g = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(2), nullable=False)
    description = db.Column(db.String(10), nullable=False)


