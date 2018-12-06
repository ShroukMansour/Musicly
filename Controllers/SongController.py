import pygame
from Controllers.AlbumController import AlbumController
from Controllers.ArtistController import ArtistController
from Controllers.BandController import BandController
from Models.Song import Song
import os
from tkinter import *
import time
import vlc

class SongController():
    def __init__(self):
        self.song = Song()

    def get_all_songs(self):
        return Song.get_all_songs(Song)

    def get_desc(self, id):
        song = self.db.get_song(id)
        return song # song info concatenated

    def playSong(self, song_path="C:\\Users\\Aya Essam\\Desktop\\MusiclyMusic\\013.mp3"):
        pygame.init()
        pygame.display.set_mode((1,1))
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play(1)
        clock = pygame.time.Clock()
        clock.tick(10)
        while pygame.mixer.music.get_busy():
            pygame.event.poll()
            clock.tick(10)

    def play_band_songs(self, band_id):
        band_songs = self.song.get_band_songs(band_id)
        for song in band_songs:
            self.playSong(song[7])

    def play_genres_songs(self, genres):
        songs = self.song.get_genres_songs(genres)
        for song in songs:
            self.playSong(song[7])

    def play_album_songs(self, album_id):
        songs = self.song.get_album_songs(album_id)
        for song in songs:
            self.playSong(song[7])

    def play_artist_songs(self, artist_id):
        songs = self.song.get_artist_songs(artist_id)
        for song in songs:
            self.playSong(song[7])

    def get_full_desc(self, id):
        song = self.song.get_song(id)
        bandcont = BandController()
        band_name = bandcont.get_band_name(song[7]) ################## band id in song
        ac = ArtistController()
        artist_name = ac.get_artist_name(song[8])  ################## artisr id in song
        abc = AlbumController()
        album_name = abc.get_album_name(song[9])  ################## artisr id in song
        return [song[1], artist_name, band_name, album_name, song[5], song[6]]##############

    def get_playlist_songs_names_duration(self, id):
        songs = self.get_playlist_songs(id)
        songs_names = []
        songs_duration = []
        for song in songs:
            songs_names.append(song[1])
            songs_duration.append(song["duration"])
        return  songs_names, songs_duration

    def get_playlist_songs(self, playlist_id):
        songs = self.song.get_playlist_songs(id)
        return songs

    def stopmusic(self):
        pygame.mixer.music.stop()

    def sort_by_name(self):
        songs = self.song.sort_by_name()
        return songs

    def sort_by_genre(self):
        songs = self.song.sort_by_genre()
        return songs

    def sort_by_release_date(self):
        songs = self.song.sort_by_release_date()
        return songs

    def sort_by_artist(self):
        songs = self.song.sort_by_artist()
        return songs

    def sort_by_album(self):
        songs = self.song.sort_by_album()
        return songs

    def add_song_to_playlist(self, song_details):
        self.song.add_song_to_playlist(song_details)
        return True

    def remove_song_from_playlist(self, song_id):
        self.song.remove_song(song_id)

#
# sc = SongController()
# sc.playSong("E:/Quran/fatha.mp3")

# import os
#
# from tkinter.filedialog import askdirectory
#
# import pygame
# from mutagen.id3 import ID3
# from tkinter import *
#
# root = Tk()
# root.minsize(300,300)
#
#
# listofsongs = []
# realnames = []
#
# v = StringVar()
# songlabel = Label(root,textvariable=v,width=35)
#
# index = 0
#
# def play_group_of_songs(self, songs_list):
#
#     directory = askdirectory()
#     os.chdir(directory)
#
#     for files in os.listdir(directory):
#         if files.endswith(".mp3"):
#
#             realdir = os.path.realpath(files)
#             audio = ID3(realdir)
#             print(files)
#             realnames.append(files)
#             listofsongs.append(files)
#
#
#     pygame.mixer.init()
#     pygame.mixer.music.load(listofsongs[0])
#     pygame.mixer.music.play()
#
# directorychooser()
#
# def updatelabel():
#     global index
#     # global songname
#     v.set(realnames[index])
#     return v
#
#
#
# def nextsong(event):
#     global index
#     index += 1
#     pygame.mixer.music.load(listofsongs[index])
#     pygame.mixer.music.play()
#     updatelabel()
#
# def prevsong(event):
#     global index
#     index -= 1
#     pygame.mixer.music.load(listofsongs[index])
#     pygame.mixer.music.play()
#     updatelabel()
#
#
# def stopsong(event):
#     pygame.mixer.music.stop()
#     v.set("")
#     return v
#
#
# label = Label(root,text='Music Player')
# label.pack()
#
# listbox = Listbox(root)
# listbox.pack()
#
# listofsongs.reverse()
# realnames.reverse()
#
# for items in realnames:
#     listbox.insert(0,items)
#
# realnames.reverse()
# listofsongs.reverse()
#
#
# nextbutton = Button(root,text = 'Next Song')
# nextbutton.pack()
#
# previousbutton = Button(root,text = 'Previous Song')
# previousbutton.pack()
#
# stopbutton = Button(root,text='Stop Music')
# stopbutton.pack()
#
#
# nextbutton.bind("<Button-1>",nextsong)
# previousbutton.bind("<Button-1>",prevsong)
# stopbutton.bind("<Button-1>",stopsong)
#
# songlabel.pack()
#
#
# root.mainloop()