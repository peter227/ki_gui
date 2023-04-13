from db import db
from sqlalchemy.orm import relationship


class AuthorsSongs(db.Model):
    id_a = db.Column(db.Integer, db.ForeignKey('authors.id_a'), nullable=False)
    id_s = db.Column(db.Integer, db.ForeignKey('songs.id_s'), nullable=False)
    author = relationship("Authors", lazy="select", backref=db.backref("Authors", lazy="joined"))
    song = relationship('Songs', lazy="select", backref=db.backref("Songs", lazy="joined"))
    created_at = db.Column(db.DateTime, nullable=True)
    updated_at = db.Column(db.DateTime, nullable=True)

