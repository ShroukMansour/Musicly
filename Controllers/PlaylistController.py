from Models.Playlist import Playlist
from Controllers.SongController import SongController
from SqliteDB.sqlite import sqlite

class PlaylistController():
    def __init__(self):
        self.sqlite = sqlite()

    def add_playlist(self, name, desc):
        self.playlist.add_playlist(name, desc)

    def getAllPlaylists(self):
        return Playlist.get_all_playlists(Playlist)

    def get_playlist_details(self, id):
        p = Playlist()
        playlist = p.get_playlist(id)
        sc = SongController()
        songs_names , songs_duration=  sc.get_playlist_songs_names_duration(id)
        return [playlist[1], playlist[1], songs_names, songs_duration]