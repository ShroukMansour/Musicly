from SqliteDB.sqlite import sqlite

class Artist:
    def __init__(self, name, dateOfBirth):
        self.name = name
        self.dateOfBirth = dateOfBirth
        self.songs = None
        self.sqlite = sqlite()

    def add_artist(self, name, dob):
        sqlite.add_artist(name, dob)

    def get_all_artist(self):
        return sqlite.get_all_artists()

