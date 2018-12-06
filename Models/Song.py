import sqlite3

from SqliteDB.sqlite import sqlite

class Song():
    con = sqlite3.connect("E:\FCI\Fourth year\Concepts\Assignments\Musicly\SqliteDB\musicly_new.db")
    c = con.cursor()
    def __init__(self, name="", Band=None, releaseDate="", genres="", lyrics="", length=0, artist_id="", album_id="", path=""):
        self.name = name
        self.band = Band
        self.featuredArtists = artist_id
        self.album = album_id
        self.releaseDate = releaseDate
        self.genres = genres
        self.lyrics = lyrics
        self.length = length
        self.path = path

    def sort_by_name(self):
        self.c.execute("SELECT * FROM song ORDER BY name ASC")
        songs = self.c.fetchall()
        self.con.commit()
        self.con.close()
        return songs

    def sort_by_genre(self):
        self.c.execute("SELECT * FROM song ORDER BY song.genres ASC")
        songs = self.c.fetchall()
        self.con.commit()
        self.con.close()
        return songs

    def sort_by_release_date(self):
        self.c.execute("SELECT * FROM song ORDER BY song.release_date ASC")
        songs = self.c.fetchall()
        self.con.commit()
        self.con.close()
        return songs

    def sort_by_album(self):
        self.c.execute("SELECT * FROM song CROSS JOIN album ON song.album_id = album.id ORDER BY album.title ASC")
        songs = self.c.fetchall()
        self.con.commit()
        self.con.close()
        return songs

    def sort_by_artist(self):
        self.c.execute("SELECT * FROM song CROSS JOIN artist ON song.artist_id = artist.id ORDER BY artist.name ASC")
        songs = self.c.fetchall()
        self.con.commit()
        self.con.close()
        return songs

    def get_song(self, id):
        self.c.execute("SELECT * FROM song where id=?", id)
        song = self.c.fetchone()
        self.con.commit()
        self.con.close()
        return song

    def get_playlist_songs(self, id):
        self.c.execute("SELECT * FROM song where playlist_id=?", (str(id),))
        songs = self.c.fetchall()
        self.con.commit()
        self.con.close()
        return songs

    def get_band_songs(self, band_id):
        self.c.execute("SELECT * FROM song where band=?", (str(band_id),))
        songs = self.c.fetchall()
        self.con.commit()
        self.con.close()
        return songs

    def get_genres_songs(self, genres):
        self.c.execute("SELECT * FROM song where genres=?", (str(genres),))
        songs = self.c.fetchall()
        self.con.commit()
        self.con.close()
        return songs

    def get_album_songs(self, album_id):
        self.c.execute("SELECT * FROM song where album_id=?", (str(album_id),))
        songs = self.c.fetchall()
        self.con.commit()
        self.con.close()
        return songs

    def get_artist_songs(self, artist_id):
        self.c.execute("SELECT * FROM song where artist_id=?", (str(artist_id),))
        songs = self.c.fetchall()
        self.con.commit()
        self.con.close()
        return songs

    def add_song_to_playlist(self, song):
        self.c.execute("INSERT INTO song (name,band,release_date,genres,lyrics,length,path,artist_id,playlist_id,album_id) VALUES  (?, ?, ?, ?,?, ?, ?, ?, ?,?)",
                       (str(song[0]),str(song[1]), str(song[2]), str(song[3]), str(song[4]),
                        str(song[5]), str(song[6]), str(song[7]), str(song[8]), str(song[9])))
        self.con.commit()
        self.con.close()

    def get_all_songs(self):
        self.c.execute("SELECT * FROM song")
        songs = self.c.fetchall()
        self.con.commit()
        self.con.close()
        return songs

    def remove_song(self, song_id):
        self.c.execute("DELETE FROM song where id=?", (song_id,))
        self.con.commit()
        self.con.close()
