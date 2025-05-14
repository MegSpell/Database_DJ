"""Forms for playlist app."""

from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Length
from flask_wtf import FlaskForm


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    # Add the necessary code to use this form

    name = StringField("Playlist Name", validators=[
        InputRequired(message="Name is required."),
        Length(max=50)
    ])
    description = TextAreaField("Description")


class SongForm(FlaskForm):
    """Form for adding songs."""

    # Add the necessary code to use this form

    title = StringField("Song Title", validators=[
        InputRequired(message="Title is required."),
        Length(max=100)
    ])
    artist = StringField("Artist", validators=[
        InputRequired(message="Artist is required."),
        Length(max=100)
    ])



# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
