from flask import Flask, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Playlist, Song, PlaylistSong
from forms import NewSongForPlaylistForm, SongForm, PlaylistForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///playlist-app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "I'LL NEVER TELL!!"

connect_db(app)
db.create_all()



# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

##############################################################################
# Homepage

@app.route("/")
def root():
    """Homepage: redirect to /playlists."""

    return redirect("/playlists")


##############################################################################
# Playlist routes


@app.route("/playlists")
def show_all_playlists():
    """Return a list of playlists."""

    playlists = Playlist.query.all()
    return render_template("playlists.html", playlists=playlists)


@app.route("/playlists/<int:playlist_id>")
def show_playlist(playlist_id):
    """Show detail on specific playlist."""

    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK

    playlist = Playlist.query.get_or_404(playlist_id)
    songs = playlist.songs  # Access PlaylistSong relationships if needed
    return render_template("playlist.html", playlist=playlist, songs=songs)
   


@app.route("/playlists/add", methods=["GET", "POST"])
def add_playlist():
    """Handle add-playlist form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-playlists
    """

    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK

    form = PlaylistForm()
    if form.validate_on_submit():
        new = Playlist(name=form.name.data, description=form.description.data)
        db.session.add(new)
        db.session.commit()
        flash("Playlist created!")
        return redirect("/playlists")
    return render_template("new_playlist.html", form=form)
   


##############################################################################
# Song routes


@app.route("/songs")
def show_all_songs():
    """Show list of songs."""

    songs = Song.query.all()
    return render_template("songs.html", songs=songs)


@app.route("/songs/<int:song_id>")
def show_song(song_id):
    """return a specific song"""

    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK

    song = Song.query.get_or_404(song_id)
    return render_template("song.html", song=song)


@app.route("/songs/add", methods=["GET", "POST"])
def add_song():
    """Handle add-song form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-songs
    """

    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK

    form = SongForm()
    if form.validate_on_submit():
        new = Song(title=form.title.data, artist=form.artist.data)
        db.session.add(new)
        db.session.commit()
        flash("Song added!")
        return redirect("/songs")
    return render_template("new_song.html", form=form)


@app.route("/playlists/<int:playlist_id>/add-song", methods=["GET", "POST"])
def add_song_to_playlist(playlist_id):
    """Add a playlist and redirect to list."""

    # BONUS - ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK
    # THE SOLUTION TO THIS IS IN A HINT IN THE ASSESSMENT INSTRUCTIONS

    playlist = Playlist.query.get_or_404(playlist_id)
    form = NewSongForPlaylistForm()

    # Restrict form to songs not already on this playlist

    #curr_on_playlist = ...
    #form.song.choices = ...

    current_song_ids = {ps.song_id for ps in playlist.songs}
    available_songs = Song.query.filter(Song.id.notin_(current_song_ids)).all()
    form.song.choices = [(song.id, song.title) for song in available_songs]


    if form.validate_on_submit():

          # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK
        new_assoc = PlaylistSong(playlist_id=playlist_id, song_id=form.song.data)
        db.session.add(new_assoc)
        db.session.commit()
        flash("Song added to playlist!")

        return redirect(f"/playlists/{playlist_id}")

    return render_template("add_song_to_playlist.html",
                             playlist=playlist,
                             form=form)


#### Stretch idea: add delete buttons for playlists and songs

@app.route("/playlists/<int:playlist_id>/delete", methods=["POST"])
def delete_playlist(playlist_id):
    playlist = Playlist.query.get_or_404(playlist_id)
    db.session.delete(playlist)
    db.session.commit()
    flash("Playlist deleted.")
    return redirect("/playlists")

@app.route("/songs/<int:song_id>/delete", methods=["POST"])
def delete_song(song_id):
    song = Song.query.get_or_404(song_id)
    db.session.delete(song)
    db.session.commit()
    flash("Song deleted.")
    return redirect("/songs")
