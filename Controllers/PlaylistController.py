from Models.Playlist import Playlist
from Controllers.SongController import SongController
from SqliteDB import sqlite

class PlaylistController():
    def __init__(self):
        self.playlist = Playlist()
        self.sqlite = sqlite()

    def addPlaylist(self):
        self.playlist.addPlaylist()

    def getAllPlaylists(self):
        return self.playlist.getAllPlaylists()

    def get_playlist_details(self, id):
        playlist = self.playlist.get_playlist(id)
        sc = SongController()
        songs_names , songs_duration=  sc.get_playlist_songs_names_duration(id)
        return [playlist[1], playlist[1], songs_names, songs_duration]