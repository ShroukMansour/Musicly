import sqlite3

from SqliteDB.sqlite import sqlite

class Artist():
    con = sqlite3.connect("E:\FCI\Fourth year\Concepts\Assignments\Musicly\SqliteDB\musicly_new.db")
    c = con.cursor()

    def __init__(self, name="", dateOfBirth=""):
        self.name = name
        self.dateOfBirth = dateOfBirth
        self.songs = None

    def add_artist(self, artist):
        self.c.execute(
            "INSERT INTO artist (name, dob, band_id) VALUES (?, ?, ?)", (artist[0], artist[1], artist[1]))
        self.con.commit()
        self.con.close()
        return True


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

    def delete_artist(self, artist_id):
        self.c.execute("DELETE FROM artist where id=?", (artist_id,))
        self.con.commit()
        self.con.close()
