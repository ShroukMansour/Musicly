from Models.Album import Album
from SqliteDB.sqlite import sqlite

class AlbumController():
    def __init__(self):
        self.sqlite = sqlite()
        self.album = Album()

    def add_album(self):
        self.album.add_album()

    def get_all_albums(self):
        s = sqlite()
        return s.get_all_albums()