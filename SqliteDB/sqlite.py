import sqlite3
class sqlite():

    def __init__(self):
        con = sqlite3.connect('musicly.db')
        c = con.cursor()

# c.execute("""CREATE TABLE songs (
#             path text PRIMARY KEY,
#             name text NOT NULL,
#             band text NOT NULL
#             )""")

# c.execute("""CREATE TABLE playlist (
#             id integer PRIMARY KEY,
#             name text NOT NULL,
#             description text NULLABLE,
#             FOREIGN KEY (songs) REFERENCES song (path)
#             )""")

# c.execute("INSERT INTO songs VALUES ('C:\\Users\\Aya Essam\\Desktop\\MusiclyMusic\\52-Al Toor.mp3','attur','afasi')")
# c.execute("SELECT * FROM songs")
# print(c.fetchall())
# con.commit()
    def getAllPlaylists(self):
        self.c.execute("SELECT * FROM playlist")
        playlists = self.c.fetchall()
        self.con.commit()
        self.con.close()
        return playlists

    def getAllSongs(self):
        self.c.execute("SELECT * FROM song")
        songs = self.c.fetchall()
        self.con.commit()
        self.con.close()
        return songs

