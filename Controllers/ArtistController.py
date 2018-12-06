from Models.Artist import Artist

class ArtistController():
    def __init__(self):
        self.artist = Artist()

    def add_artist(self, artist_details):
        self.artist.add_artist(artist_details)

    def get_all_artist(self):
        return self.artist.get_all_artist()

    def get_artists_names(self):
        artists_list = self.get_all_artist()
        artists_names = []
        for artist in artists_list:
            artists_names.append(artist[1])
        return artists_names

    def get_artist(self, id):
        return self.artist.get_artist(id)

    def get_artist_name(self, id):
        artist = self.get_artist(id)
        return artist[1]

    def delete_artist(self, artist_id):
        self.artist.delete_artist(artist_id)
