import sqlite3

from SqliteDB.sqlite import sqlite

class Song():
    def __init__(self, name, Band, releaseDate, genres, lyrics, length, artist_id, album_id, path):
        self.name = name
        self.band = Band
        self.featuredArtists = artist_id
        self.album = album_id
        self.releaseDate = releaseDate
        self.genres = genres
        self.lyrics = lyrics
        self.length = length
        self.path = path
        self.con = sqlite3.connect('E:\FCI\Fourth year\Concepts\Assignments\Musicly\SqliteDB\musicly_new.db')
        self.c = self.con.cursor()


    def get_song(self, id):
        return self.db.get_song(id)

    def add_song_to_playlist(self, playlist_id, song):
        self.c.execute("INSERT INTO song VALUES (?, ?, ?, ?, ?,?, ?, ?, ?, ?)",
                       (song[0], song[1], song[2], song[3], song[4], song[5], song[6], song[7], song[8], song[9]))
        self.con.commit()
        self.con.close()