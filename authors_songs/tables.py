from db import db

authors_songs = db.Table('authors_songs',
                         db.Column('id_a', db.Integer, db.ForeignKey('authors.id_a'), primary_key=True, nullable=False),
                         db.Column('id_s', db.Integer, db.ForeignKey('songs.id_s'), primary_key=True, nullable=False),
                         db.Column('created_at', db.DateTime, nullable=True),
                         db.Column('updated_at', db.DateTime, nullable=True)
                         )
