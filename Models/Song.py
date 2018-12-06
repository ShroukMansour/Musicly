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
        self.con = sqlite3.connect("C:\\Users\\Aya Essam\\anaconda3\\MusiclyNew\\Musicly\\SqliteDB\\musicly_new.db")
        self.c = self.con.cursor()


    def get_song(self, id):
        self.c.execute("SELECT * FROM song where id=?", id)
        song = self.c.fetchone()
        self.con.commit()
        self.con.close()
        return song

    def get_playlist_songs(self, id):
        self.c.execute("SELECT * FROM song where playlist_id=?", id)
        songs = self.c.fetchall()
        self.con.commit()
        self.con.close()
        return songs


    def add_song_to_playlist(self, playlist_id, song):
        self.c.execute("INSERT INTO song VALUES (?, ?, ?, ?, ?,?, ?, ?, ?, ?)",
                       (song[0], song[1], song[2], song[3], song[4], song[5], song[6], song[7], song[8], song[9]))
        self.con.commit()
        self.con.close()