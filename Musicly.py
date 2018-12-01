import numpy as np
from Controllers import  SongController as  sc
from Controllers import  PlaylistController as  pc
from Models import Playlist, Song, Album, Artist, Band
class Musicly():
    def __init__(self):
        self.artist = np.array
        self.band =  np.array
        self.playlists = np.array(Playlist)
        self.songs = np.array(Song)


    def viewPlaylists(self):
        playlists =  pc.PlaylistController.getAllPlaylists(pc)
        for pl in playlists:
            print(pl.getName())
            print("     tracks: " + pl.getTracks())

    def viewSongs(self):
        songs = sc.songController.getAllSongs(sc)
        for s in songs:
            print(s)

my = Musicly()
my.viewPlaylists()

