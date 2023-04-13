from db import db
from sqlalchemy.orm import relationship


class Playlists(db.Model):
    id_p = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id_u'), nullable=False)
    user = relationship("Users", lazy="select", backref=db.backref('Users', lazy='joined'))
    number_of_songs = db.Column(db.Integer, nullable=False)
    length_sec = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(40), nullable=False)
    private = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=True)
    updated_at = db.Column(db.DateTime, nullable=True)


class PlaylistsSongs(db.Model):
    id_p = db.Column(db.Integer, nullable=False)
    playlist = relationship("Playlists", lazy="select", backref=db.backref("Playlists", lazy="joined"))
    id_s = db.Column(db.Integer, nullable=False)
    songs = relationship("Songs", lazy="select", backref=db.backref("Songs", lazy="joined"))
    created_at = db.Column(db.DateTime, nullable=True)
    updated_at = db.Column(db.DateTime, nullable=True)