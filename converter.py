import tkinter
import tkinter as Tk
import customtkinter
from tkinter import filedialog as fp
from tkinter.ttk import *
import moviepy.editor as mp
import os

root = Tk.Tk()
root.geometry("500x400")
root.configure(background='#082350')
root.title("Mp3 Converter")


def Add_Files():

	file = fp.askopenfile(mode='r', filetypes=[('Video Files', '.mp4')])
	if file:
		flpath = os.path.abspath(file.name)

	new = os.path.basename(flpath).split('/')[-1]
	print(type(new))

	vid = mp.VideoFileClip(new)
	b = new.split('.mp4')[:1]

	def Convert():
		
		for i in b:			
			vid.audio.write_audiofile(i+".mp3")

	ent.insert("end", b)

	btn = customtkinter.CTkButton(master=root, text='Convert', corner_radius=8, command=Convert)
	btn.pack(pady=10)




label1 = customtkinter.CTkLabel(root,  width=450, height=200)
label1.pack()
label1.pack_propagate(False)

prg = Progressbar(label1)
prg.pack()

ent = customtkinter.CTkEntry(root, width=400, corner_radius=15, height=40, fg_color=('#b1bbb1', '#202220'))
ent.pack()



btn = customtkinter.CTkButton(master=root, text='Browse Files..', corner_radius=8, command=Add_Files)
btn.pack(pady=10)

root.mainloop()