import numpy as np
from Controllers import  SongController as  sc
from Models import Playlist, Song, Album, Artist, Band
class Musicly():
    def __init__(self):
        self.artist = np.array
        self.band =  np.array
        self.playlists = np.array(Playlist)
        self.songs = np.array(Song)
        # self.playlistController = PlaylistController.PlaylistController()
        # self.songController = sc()


    def viewPlaylists(self):
        playlists =  self.playlistController.getAllPlaylists()
        for pl in playlists:
            print(pl.getName())
            print("     tracks: " + pl.getTracks())

    def viewSongs(self):
        songs = sc.songController.getAllSongs(sc)
        for s in songs:
            print(s)

my = Musicly()
my.viewSongs()

