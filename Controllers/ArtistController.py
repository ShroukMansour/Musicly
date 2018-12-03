from Models.Artist import Artist

class ArtistController():
    def __init__(self):
        self.artist = Artist()

    def add_artist(self):
        self.artist.add_artist()

    def get_all_artist(self):
        return self.artist.get_all_artist()