import sqlite3
from Models.Song import Song

class Playlist():

    con = sqlite3.connect("C:\\Users\\Aya Essam\\anaconda3\\MusiclyNew\\Musicly\\SqliteDB\\musicly_new.db")
    c = con.cursor()

    def __init__(self, name="", description=""):
        self.name = name
        self.songs = []
        self.description = description
        self.tracks = 0

    def getName(self):
        return self.name

    def getTracks(self):
        return self.tracks

    def add_playlist(self, name, desc):
        self.c.execute("INSERT INTO playlist VALUES (?, ?)",(name, desc))
        self.con.commit()
        self.con.close()
        return


    def getPlaylist(self, name):
        #sqlite get playlists by name //assume each playlist has unique name
        self.tracks = len(self.songs)
        return self

    def get_playlist_songs(self, id):
        self.c.execute("SELECT * FROM song where playlist_id=?", str(id))
        songs = self.c.fetchall()
        for s in songs:
            self.songs.append(Song(s[1], s[2], s[3], s[4], s[5], s[6], s[8], s[10]))
        self.con.commit()
        self.con.close()

    def get_playlist(self, id):
        self.c.execute("SELECT * FROM playlist where id=?", (str(id),))
        x = self.c.fetchone()
        self.con.commit()
        self.con.close()
        return x

    def get_all_playlists(self):
        self.c.execute("SELECT * FROM playlist")
        playlists = self.c.fetchall()
        self.con.commit()
        self.con.close()
        return playlists

    def delete_playlist(self, playlist_id):
        self.c.execute("DELETE FROM playlist where id=?", (playlist_id,))
        self.con.commit()
        self.con.close()
