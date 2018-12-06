import sqlite3

class sqlite():

    def __init__(self):
        self.con = sqlite3.connect('E:\FCI\Fourth year\Concepts\Assignments\Musicly\SqliteDB\musicly_new.db')
        self.c = self.con.cursor()



    def getAllSongs(self):
        self.c.execute("SELECT * FROM song")
        songs = self.c.fetchall()
        self.con.commit()
        self.con.close()
        return songs

    def get_song(self, id):
        self.c.execute("SELECT * FROM song where id=?", (id))
        song = self.c.fetchall()
        self.con.commit()
        self.con.close()
        return song



    def addSongToSongs(self, path, name, band):
        self.c.execute(
            "INSERT INTO song VALUES (?, ?, ?)",(name, band, path))
        self.con.commit()

    def add_artist(self, name, dob):
        self.c.execute(
            "INSERT INTO artist VALUES (?, ?)", (name, dob))
        self.con.commit()

#s = sqlite()
#s.createTable()
#s.addSongToSongs("c:/songs/3","yaseen", "hazaa")
#print(s.getAllSongs())

# def createTable(self):
#     self.c.execute("""CREATE TABLE playlist (
#                 id integer PRIMARY KEY,
#                 name text NOT NULL,
#                 description text NULLABLE
#                 )""")
#     self.c.execute("""CREATE TABLE songs (
#                 path text PRIMARY KEY,
#                 name text NOT NULL,
#                 band text NOT NULL
#                 )""")

# CREATE TABLE `song` (
# 	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
# 	`name`	TEXT,
# 	`band`	TEXT,
# 	`path`	TEXT NOT NULL,
# 	`playlist_id`	INTEGER,
# 	FOREIGN KEY (playlist_id) REFERENCES playlist(id)
# );

