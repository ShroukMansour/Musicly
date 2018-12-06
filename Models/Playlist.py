import sqlite3
from Models.Song import Song
import numpy as np
from Models.Song import Song


class Playlist:
    def __init__(self):
        self.name = ""
        self.songs = []
        self.description = ""
        self.tracks = 0
        self.con = sqlite3.connect('E:\FCI\Fourth year\Concepts\Assignments\Musicly\SqliteDB\musicly_new.db')
        self.c = self.con.cursor()

    def __init__(self, name, description):
        self.playlist = Playlist()
        self.name = name
        self.songs = []
        self.description = description
        self.tracks = 0
        self.con = sqlite3.connect('E:\FCI\Fourth year\Concepts\Assignments\Musicly\SqliteDB\musicly_new.db')
        self.c = self.con.cursor()

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
        self.c.execute("SELECT * FROM playlist where id=?", id)
        x = self.c.fetchone()
        self.con.commit()
        self.con.close()
        return x

    def getAllPlaylists(self):
        self.c.execute("SELECT * FROM playlist")
        playlists = self.c.fetchall()
        self.con.commit()
        self.con.close()
        return playlists
