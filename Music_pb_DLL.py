import pygame
from tkinter import *
from tkinter import ttk

class Song:
    def __init__(self, title, artist, file_path):
        self.title = title
        self.artist = artist
        self.file_path = file_path
        self.next = None
        self.prev = None

class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current_song = None
        self.paused = False

    def add_song(self, title, artist, file_path):
        new_song = Song(title, artist, file_path)
        if not self.head:
            self.head = new_song
            self.tail = new_song
            self.current_song = new_song
        else:
            self.tail.next = new_song
            new_song.prev = self.tail
            self.tail = new_song

    def play_current_song(self):
        if self.current_song:
            pygame.mixer.music.load(self.current_song.file_path)
            pygame.mixer.music.play()
            print(f"Now playing: {self.current_song.title} by {self.current_song.artist}")
            self.paused = False
        else:
            print("No song is selected.")

    def play_next_song(self):
        if self.current_song and self.current_song.next:
            self.current_song = self.current_song.next
            self.play_current_song()
        else:
            print("No next song available.")

    def play_previous_song(self):
        if self.current_song and self.current_song.prev:
            self.current_song = self.current_song.prev
            self.play_current_song()
        else:
            print("No previous song available.")

    def pause_song(self):
        pygame.mixer.music.pause()
        self.paused = True
        print("Song paused.")

    def resume_song(self):
        if self.paused:
            pygame.mixer.music.unpause()
            print("Song resumed.")
            self.paused = False
        else:
            print("No song is paused.")

    def stop_song(self):
        pygame.mixer.music.stop()
        print("Song stopped.")

    def print_playlist(self):
        current_song = self.head
        print("Playlist:")
        while current_song:
            print(f"{current_song.title} by {current_song.artist}")
            current_song = current_song.next

# Initialize pygame mixer
pygame.mixer.init()

# Create Playlist instance
playlist = Playlist()

# Add songs to the playlist
playlist.add_song("Song 1", "Artist 1", "song1.mp3")
playlist.add_song("Song 2", "Artist 2", "song2.mp3")
playlist.add_song("Song 3", "Artist 3", "song3.mp3")

# Function to play the current song
def play_current():
    playlist.play_current_song()

# Function to play the next song
def play_next():
    playlist.play_next_song()

# Function to play the previous song
def play_previous():
    playlist.play_previous_song()

# Function to pause the current song
def pause():
    playlist.pause_song()

# Function to resume the paused song
def resume():
    playlist.resume_song()

# Function to stop the current song
def stop():
    playlist.stop_song()

# Function to print all songs in the playlist
def print_all_songs():
    playlist.print_playlist()

# Create a Tkinter window
root = Tk()
root.title("Music Player")

# Create buttons for song control
btn_previous = Button(root, text="Previous", command=play_previous)
btn_previous.pack(side=LEFT, padx=10, pady=10)

btn_play = Button(root, text="Play", command=play_current)
btn_play.pack(side=LEFT, padx=10, pady=10)

btn_next = Button(root, text="Next", command=play_next)
btn_next.pack(side=LEFT, padx=10, pady=10)

btn_pause = Button(root, text="Pause", command=pause)
btn_pause.pack(side=LEFT, padx=10, pady=10)

btn_resume = Button(root, text="Resume", command=resume)
btn_resume.pack(side=LEFT, padx=10, pady=10)

btn_stop = Button(root, text="Stop", command=stop)
btn_stop.pack(side=LEFT, padx=10, pady=10)

btn_print = Button(root, text="Print Playlist", command=print_all_songs)
btn_print.pack(side=LEFT, padx=10, pady=10)

root.mainloop()
