from app import app
from models import db, Playlist, Song, PlaylistSong

# Drop & recreate tables
db.drop_all()
db.create_all()

# 🎭 Playlists
broadway = Playlist(name="Broadway Hits", description="Show-stoppers from Broadway musicals")
movies = Playlist(name="Movie Songs", description="Iconic tracks from movie musicals")

# 🎶 Songs from Broadway (Wicked + Hamilton)
s1 = Song(title="Defying Gravity", artist="Idina Menzel (Wicked)")
s2 = Song(title="Popular", artist="Kristin Chenoweth (Wicked)")
s3 = Song(title="My Shot", artist="Lin-Manuel Miranda (Hamilton)")
s4 = Song(title="Wait For It", artist="Leslie Odom Jr. (Hamilton)")

# 🎬 Songs from The Greatest Showman
s5 = Song(title="This Is Me", artist="Keala Settle")
s6 = Song(title="Rewrite the Stars", artist="Zac Efron & Zendaya")
s7 = Song(title="The Greatest Show", artist="Hugh Jackman & Cast")

# Add all to session
db.session.add_all([
    broadway, movies,
    s1, s2, s3, s4, s5, s6, s7
])
db.session.commit()

# Playlist-Song associations
db.session.add_all([
    PlaylistSong(playlist_id=broadway.id, song_id=s1.id),
    PlaylistSong(playlist_id=broadway.id, song_id=s2.id),
    PlaylistSong(playlist_id=broadway.id, song_id=s3.id),
    PlaylistSong(playlist_id=broadway.id, song_id=s4.id),

    PlaylistSong(playlist_id=movies.id, song_id=s5.id),
    PlaylistSong(playlist_id=movies.id, song_id=s6.id),
    PlaylistSong(playlist_id=movies.id, song_id=s7.id),
])
db.session.commit()

print("🌱 Seeded with show tunes and cinematic bangers!")
