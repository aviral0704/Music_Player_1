import tkinter
import pygame
from tkinter.filedialog import askdirectory
import os

player= tkinter.Tk()
player.title("Music Player")
player.geometry("500x300")


var = tkinter.StringVar()
var.set("Select the Song to Play")

os.chdir(askdirectory())
songlist = os.listdir()


playing = tkinter.Listbox(player,font= "Helvetica 12 bold", width = 60, bg = "black", fg = "white",selectmode = tkinter.SINGLE)
for item in songlist:
    playing.insert(0, item)

pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(playing.get(tkinter.ACTIVE))
    name = playing.get(tkinter.ACTIVE)
    var.set(f"{name[:16]}..." if len(name)>18 else name)
    pygame.mixer.music.play()

def pause():
    pygame.mixer.music.pause()

def resume():
    pygame.mixer.music.unpause()

text = tkinter.Label(player, font= "Helvetica", textvariable=var).grid(row=0, columnspan=3)
playing.grid(columnspan=3)

playB = tkinter.Button(player,width=6, height=1, font="Helvetica",text="play", command=play,bg="green").grid(row=2,columnspan=1)
pauseB = tkinter.Button(player, width=6, height=1, font="Helvetica",text="pause", command=pause,bg="red").grid(row=2,columnspan=2)
resumeB = tkinter.Button(player,width=6, height=1, font="Helvetica",text="resume", command=resume,bg="yellow").grid(row=2,columnspan=3)

player.mainloop()