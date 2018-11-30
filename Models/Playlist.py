import numpy as np
class Playlist:
    def __init__(self, name, description):
        self.name = name
        self.songs = np.array()
        self.description = description
        self.tracks = 0

    def getName(self):
        return self.name

    def getTracks(self):
        return self.tracks

    def addPlaylist(self, name, desc, songs):
        #asqlite dds playlist
        return

    def getPlaylist(self, name):
        #sqlite get playlists by name //assume each playlist has unique name
        self.tracks = len(self.songs)
        return self