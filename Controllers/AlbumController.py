from Models.Album import Album
from SqliteDB.sqlite import sqlite

class AlbumController():
    def __init__(self):
        self.sqlite = sqlite()
        self.album = Album()

    def add_album(self):
        self.album.add_album()

    def get_all_albums(self):
        return self.album.get_all_albums()


    def get_album(self, id):
        return self.artist.get_artist(id)

    def get_album_name(self, id):
        x = self.get_album(id)
        return x[1]
