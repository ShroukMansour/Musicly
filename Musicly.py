import numpy as np
from Controllers.SongController import SongController
from Controllers.PlaylistController import PlaylistController
from Controllers.AlbumController import AlbumController
from Controllers.ArtistController import ArtistController
from Models.Playlist import Playlist
from Models.Song import Song
from Models.Album import Album

class Musicly():
    def __init__(self):
        self.artist = np.array
        self.band =  np.array
        self.playlists = np.array(Playlist)
        self.songs = np.array(Song)
        self.albums = np.array(Album)
        self.playlist_controller = PlaylistController()


    def viewPlaylists(self):
        pc = PlaylistController()
        self.playlists = pc.getAllPlaylists()
        for i in range(len(self.playlists)):
            self.playlists[i] = Playlist(self.playlists[i][1], self.playlists[i][2])
            print(self.playlists[i].getName())
            print("tracks: " , self.playlists[i].getTracks())

    def viewSongs(self):
        sc = SongController()
        self.songs = sc.get_all_songs()
        for s in self.songs:
            print(s)

    def view_albums(self):
        ac = AlbumController()
        self.albums = ac.get_all_albums()
        for a in self.albums:
            print(a)

    def view_artists(self):
        ass = ArtistController()
        self.artists = ass.get_all_artist()
        for a in self.artists:
            print(a)

    def get_playlist_details(self, id):
        playlist_details  = self.playlist_controller.get_playlist_details(id)
        return playlist_details

    def play_artist_songs(self, album_id):
        sc = SongController()
        songs = sc.play_album_songs(album_id)

    def play_band_songs(self, band_id):
        sc = SongController()
        songs = sc.play_band_songs(band_id)

    def play_genres_songs(self, genres):
        sc = SongController()
        songs = sc.play_genres_songs(genres)

    def play_artist_songs(self, artist_id):
        sc = SongController()
        songs = sc.play_artist_songs(artist_id)

    def add_playlist(self, name, desc):
        pc = PlaylistController()
        pc.add_playlist(name, desc)

    def add_song_to_playlist(self, playlist_id):
        pc = PlaylistController()
        pc.add_playlist(name, desc)



my = Musicly()
# my.viewPlaylists()
# my.viewSongs()
# my.view_albums()
# my.view_albums()
# print(my.get_playlist_details(2))
my.play_band_songs(1)