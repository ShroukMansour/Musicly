import sqlite3


class Band():
    def __init__(self, name):
        self.songs = None
        self.name = name
        self.con = sqlite3.connect("C:\\Users\\Aya Essam\\anaconda3\\MusiclyNew\\Musicly\\SqliteDB\\musicly_new.db")
        self.c = self.con.cursor()

    def get_band(self, id):
        self.c.execute("SELECT * FROM band where id=?", id)
        band = self.c.fetchone()
        self.con.commit()
        self.con.close()
        return band
