from Models.Playlist import Playlist
from SqliteDB import sqlite

class PlaylistController():
    def __init__(self):
        self.playlist = Playlist()
        self.sqlite = sqlite()

    def addPlaylist(self):
        self.playlist.addPlaylist()

    def getAllPlaylists(self):
        s = sqlite.sqlite()
        return s.getAllPlaylists()