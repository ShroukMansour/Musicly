import numpy as np
from Controllers import SongController as sc
from Controllers import PlaylistController as pc
from Controllers.AlbumController import AlbumController
from Controllers.ArtistController import ArtistController
from Models.Playlist import Playlist
from Models.Song import Song
from Models.Album import Album
from Models.Artist import Artist
from Models.Band import Band




class Musicly():
    def __init__(self):
        self.artist = np.array
        self.band =  np.array
        self.playlists = np.array(Playlist)
        self.songs = np.array(Song)
        self.albums = np.array(Album)


    def viewPlaylists(self):
        self.playlists = pc.PlaylistController.getAllPlaylists(pc)
        for i in range(len(self.playlists)):
            self.playlists[i] = Playlist(self.playlists[i][1], self.playlists[i][2])
            print(self.playlists[i].getName())
            print("tracks: " , self.playlists[i].getTracks())

    def viewSongs(self):
        self.songs = sc.songController.getAllSongs(sc)
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




my = Musicly()
# my.viewPlaylists()
# my.viewSongs()
my.view_albums()
