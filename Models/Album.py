import sqlite3


class Album():


    def __init__(self, songs=None):
        self.songs = songs
        self.con = sqlite3.connect("C:\\Users\\Aya Essam\\anaconda3\\MusiclyNew\\Musicly\\SqliteDB\\musicly_new.db")
        self.c = self.con.cursor()

    def get_all_albums(self):
        self.c.execute("SELECT * FROM album")
        albums = self.c.fetchall()
        self.con.commit()
        self.con.close()
        return albums

    def get_album(self, id):
        self.c.execute("SELECT * FROM album where id=?", str(id))
        x = self.c.fetchone()
        self.con.commit()
        self.con.close()
        return x