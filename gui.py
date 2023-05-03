from tkinter import *
import tkinter as Tk
from tkvideo import tkvideo
from tkinter.ttk import Progressbar
from tkvideo import *
from tkinter import filedialog
from tkinter.messagebox import showinfo
import customtkinter
from PIL import ImageTk, Image
import sqlite3
from sqlite3 import Error
import os
import pygame
import time



gui = Tk.Tk()
gui.geometry("850x650")
gui.configure(bg="#1e221e")
gui.title("Multimedia Player")

pygame.mixer.init()

photo = PhotoImage(file='piano.png')
gui.iconphoto(False, photo)

#toggle fullscreen
def Full_screen():

	gui.attributes('-fullscreen', True)
	
def Noep():
	emptywin = Toplevel()
	emptywin.geometry("200x200")

	label = Label(emptywin, text="Hiii")
	label.pack()



#menubar

menubar = Menu(gui)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='Exit', command=gui.destroy)
filemenu.add_separator()
filemenu.add_command(label='Save Playlist', command=Noep)
filemenu.add_command(label='Save as', command=Noep)
filemenu.add_command(label='Open..', command=Noep)


playlistmenu = Menu(menubar, tearoff=0)
playlistmenu.add_command(label='New', command=Noep)


helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label='Help options', command=Noep)
helpmenu.add_separator()

viewmenu = Menu(menubar, tearoff=0)
viewmenu.add_command(label='Fullscreen', command=Full_screen)
viewmenu.add_separator()
viewmenu.add_command(label='Now Playing', command=Noep)


menubar.add_cascade(label='File', menu=filemenu)
menubar.add_cascade(label='Playlists', menu=playlistmenu)
menubar.add_cascade(label='Help', menu=helpmenu)
menubar.add_cascade(label='View', menu=viewmenu)


gui.configure(menu=menubar)



Larger_frame = Frame(gui, bg='#2c322c', width=830, height=596)
Larger_frame.pack(fill=BOTH)
Larger_frame.pack_propagate(False)

#serach entry frame
search_frame = Frame(Larger_frame, bg="#202020", height=35)
search_frame.pack(fill=X)

st = customtkinter.CTkEntry(master=search_frame, fg_color=('white', '#202020'), width=250, corner_radius=15)
st.pack(pady=10, padx=130)

#divider borders
divider = Frame(Larger_frame, width=2, height=600, bg='grey')
divider.place(x=280, y=50)

#navigation pane
nav_frame = Frame(Larger_frame, width=270, height=480, bg='#363c36', borderwidth=4)
nav_frame.pack(side=LEFT, fill=Y)
nav_frame.pack_propagate(False)


#nav pane labels
n1=Label(nav_frame, text="__Playing List__", bg='#131813', foreground='#a1b5a1', font=('arial', 9, 'bold'))
n1.pack(fill=X, ipady=4)

n2=Label(nav_frame, width=38, height=28, bg='#1d241d')
n2.pack(pady=1)
n2.pack_propagate(False)


#player Frame
media = Frame(Larger_frame, width=550, height=450, bg='#9fa59f')
media.pack(pady=4)
media.pack_propagate(False)



ml = customtkinter.CTkLabel(master=media, text='Player', width=390, height=300, corner_radius=10, fg_color=('#0d140d', '#0d140d'))
ml.pack(pady=10)
ml.pack_propagate(False)

img_label = Label(ml, width=350, text='', height=270, bg='#0d140d')
img_label.pack(pady=7)
img_label.pack_propagate(False)



songs = []
curr_song = ''
paused = False

def Load_music():
	global curr_song

	gui.directory = filedialog.askdirectory()

	for song in os.listdir(gui.directory):
		name, ext = os.path.splitext(song)

		if ext == '.mp3':
			songs.append(song )

	for song in songs:
		songs_list.insert("end", song)
	
	songs_list.selection_set(0)
	curr_song = songs[songs_list.curselection()[0]]


def play_music():
	global curr_song, paused
	if not paused:
		pygame.mixer.music.load(os.path.join(gui.directory, curr_song))
		pygame.mixer.music.play()

		while not paused:
			for i in range(350):
				progress['value'] +=1 
				gui.update_idletasks()
				time.sleep(2)
	

def pause_music():
	global paused

	pygame.mixer.music.pause()
	paused=True
	while paused:
		progress.pause()
		progress['value'] = (time.time())/350

progress = Progressbar(img_label, orient=HORIZONTAL, length=300, mode='determinate')
progress.pack()

#player_control label
pcl = Label(media, width=40, height=6, bg='#9fa59f', borderwidth=4)
pcl.pack()
pcl.pack_propagate(False)

# buttons
playbtn_img = PhotoImage(file='playbtn.png')
pausebtn_img = PhotoImage(file='pausebtn.png')


playbtn = Button(pcl, image=playbtn_img, text='play_music', width=80, height=71, borderwidth=0, bg='#9fa59f', command=play_music)
playbtn.place(x=56, y=10)

#pausebtn
pausebtn = Button(pcl, image=pausebtn_img, text='play_music', width=80, height=70, borderwidth=0, bg='#9fa59f', command=pause_music)
pausebtn.place(x=148, y=10)

#songs list

songs_list = Listbox(n2, selectmode=SINGLE,  height=20, width=50, fg="#edf3ff", bg='#2d3036')
songs_list.pack()
songs_list.pack_propagate(False)

#list scroller
scroll = Scrollbar(songs_list, bg='#162f6c' ,command=songs_list.yview)
songs_list.configure(yscrollcommand=scroll.set)
scroll.pack(side=RIGHT, fill=Y)


nfilebutt = customtkinter.CTkButton(master=media, text="Browse files...", width=40, command=Load_music)
nfilebutt.pack()


gui.mainloop()
