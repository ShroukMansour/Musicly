import sqlite3

from SqliteDB.sqlite import sqlite

class Artist():
    def __init__(self, name, dateOfBirth):
        self.name = name
        self.dateOfBirth = dateOfBirth
        self.songs = None
        self.con = sqlite3.connect("C:\\Users\\Aya Essam\\anaconda3\\MusiclyNew\\Musicly\\SqliteDB\\musicly_new.db")
        self.c = self.con.cursor()
        self.sqlite = sqlite()

    def add_artist(self, name, dob):
        sqlite.add_artist(name, dob)


    def get_all_artists(self):
        self.c.execute("SELECT * FROM artists")
        artists = self.c.fetchall()
        self.con.commit()
        self.con.close()
        return artists

    def get_artist(self, id):
        self.c.execute("SELECT * FROM artist where id=?", id)
        x = self.c.fetchone()
        self.con.commit()
        self.con.close()
        return x
