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

    def add_song_to_playlist(self):
        sc = SongController()
        playlist_id = 2
        song_details = ["shrouk", 'band', 'data', 'sad','lyrics', '50', 'E:\\Quran\\falq.mp3',
                       1, playlist_id, 1  ] # see if artist_id num or name
        sc.add_song_to_playlist(song_details)

    def add_artist(self):
        ac = ArtistController()
        artist_details = ['shrouk', '10/12', 1]
        ac.add_artist(artist_details)

    def add_album(self):
        ac = AlbumController()
        album_details = ['shrouk', 1]
        ac.add_album(album_details)

    def remove_song_from_playlist(self):
        sc = SongController()
        song_id = 3
        sc.remove_song_from_playlist(song_id)

    def delete_playlist(self):
        pc = PlaylistController()
        playlist_id = 3
        pc.delete_playlist(playlist_id)

    def delete_song(self):
        sc = SongController()
        song_id = 3
        sc.remove_song_from_playlist(song_id)

    def delete_album(self):
        ac = AlbumController()
        album_id = 2
        ac.delete_album(album_id)

    def delete_artist(self):
        ac = ArtistController()
        artist_id = 3
        ac.delete_artist(artist_id)

    def sort_by_name(self):
        sc = SongController()
        songs = sc.sort_by_name()
        return songs

    def sort_by_album(self):
        sc = SongController()
        songs = sc.sort_by_album()
        return songs

    def sort_by_artist(self):
        sc = SongController()
        songs = sc.sort_by_artist()
        return songs

    def sort_by_release_date(self):
        sc = SongController()
        songs = sc.sort_by_release_date()
        return songs

    def sort_by_genre(self):
        sc = SongController()
        songs = sc.sort_by_genre()
        return songs


my = Musicly()
# my.viewPlaylists()
# my.viewSongs()
# my.view_albums()
# my.view_albums()
# print(my.get_playlist_details(2))
# my.play_band_songs(1)
# my.add_song_to_playlist()
# my.add_artist()
# my.add_album()
# my.remove_song_from_playlist()
# my.delete_playlist()
# my.delete_song()
#my.delete_album()
# my.delete_artist()
# print(my.sort_by_album())
