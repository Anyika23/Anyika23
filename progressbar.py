from tkinter import *
from tkinter.ttk import *
import tkinter as Tk
import time


root = Tk.Tk()
root.geometry("600x400")


def Show():
	
	for i in range(5):
		
		progress['value'] +=20
		label.config(text=progress['value'])
		root.update_idletasks()
		time.sleep(1)
def Stop():
	progress.stop()


progress = Progressbar(root, orient=HORIZONTAL, length=300, mode='determinate')
progress.pack()


btn = Button(root, text='Start', command=Show)
btn.pack()

btn2 = Button(root, text='Stop', command=Stop)
btn2.pack()

label = Label(root, text="")
label.pack()

root.mainloop()