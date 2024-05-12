from . import db
from flask_login import UserMixin
from sqlalchemy.orm import relationship

class LikedSongs(db.Model):
    __tablename__ = 'liked_songs'

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey('song.id'), primary_key=True)

    # Define relationship with User and Song models
    user = relationship('User', backref='liked_songs')
    song = relationship('Song', backref='liked_by')

    def __repr__(self):
        return f"User {self.user_id} liked Song {self.song_id}"


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    name = db.Column(db.String(150), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    is_artist = db.Column(db.Boolean, nullable=False)

    songs = relationship('Song', backref='artist', lazy=True)


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    release_date = db.Column(db.Date)
    artist_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
