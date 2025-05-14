"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""

    # ADD THE NECESSARY CODE HERE

    __tablename__ = 'playlist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)

    # Optional: relationship to PlaylistSong
    songs = db.relationship('PlaylistSong', backref='playlist', cascade="all, delete-orphan")



class Song(db.Model):
    """Song."""

    # ADD THE NECESSARY CODE HERE

    __tablename__ = 'song'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)

    # Optional: relationship to PlaylistSong
    playlists = db.relationship('PlaylistSong', backref='song', cascade="all, delete-orphan")



class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    # ADD THE NECESSARY CODE HERE

    __tablename__ = 'playlist_song'

    playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'), primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey('song.id'), primary_key=True)


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
