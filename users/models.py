from db import db
from genders.models import Genders
from sqlalchemy.orm import relationship


class Users(db.Model):
    id_u = db.Column(db.Integer, primary_key=True)
    profile_name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    date_of_birth = db.Column(db.DateTime, nullable=False)
    gender = db.Column(db.Integer, db.ForeignKey(Genders.id_g), nullable=False)
    gender_f = db.relationship("Genders", lazy="select", backref=db.backref("Genders", lazy="joined"))
    created_at = db.Column(db.DateTime, nullable=True)
    updated_at = db.Column(db.DateTime, nullable=True)
