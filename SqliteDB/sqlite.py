import sqlite3
class sqlite():

    def __init__(self):
        self.con = sqlite3.connect('musicly.db')
        self.c = self.con.cursor()

    def getAllPlaylists(self):
        self.c.execute("SELECT * FROM playlist")
        playlists = self.c.fetchall()
        self.con.commit()
        self.con.close()
        return playlists

    def getAllSongs(self):
        self.c.execute("SELECT * FROM songs")
        songs = self.c.fetchall()
        self.con.commit()
        self.con.close()
        return songs

    def createTable(self):
        self.c.execute("""CREATE TABLE playlist (
                    id integer PRIMARY KEY,
                    name text NOT NULL,
                    description text NULLABLE
                    )""")
        # self.c.execute("""CREATE TABLE songs (
        #             path text PRIMARY KEY,
        #             name text NOT NULL,
        #             band text NOT NULL
        #             )""")
    def addSongToSongs(self, path, name, band):
        self.c.execute(
            "INSERT INTO songs VALUES (?, ?, ?)",(path, name, band))
        self.con.commit()

# c.execute("""CREATE TABLE playlist (
#             id integer PRIMARY KEY,
#             name text NOT NULL,
#             description text NULLABLE,
#             FOREIGN KEY (songs) REFERENCES song (path)
#             )""")

#
s = sqlite()
# s.createTable()
# s.addSongToSongs("c:/songs/YASEEN","yaseen", "hazaa")
# s.addSongToSongs("c:/songs/TAHA","taha", "afasi")
# s.addSongToSongs("c:/songs/alfajr","alfajr", "hazaa")

# print(s.getAllSongs())