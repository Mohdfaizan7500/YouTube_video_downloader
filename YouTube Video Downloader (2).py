
#first you want to install all this  libraries
#install os by( pip install os-win)
import os
#install YouTube by (pip install pytube)
from pytube import YouTube, exceptions
# intall time by(pip install TIME-python)
from time import time
from tkinter import *
# install customtkinter(pip install customtkinter)
from customtkinter import *

# Download video function
def download_video(entry_field):
    print("sgdgu")
    
    ask = CTk
    ask.title("Asked")
    ask.geometry("300x100")
    ask.grid_rowconfigure((0,1), weight=1)
    ask.grid_columnconfigure(0, weight=1)
    ask_label = CTkLabel(error, text="Select Your Choice")
    ask_label.grid(row=0, column=0)
    ask = CTkButton(ask, text="OK", command=None)
    ask.grid(row=1, column=0)
    ask.mainloop()
        
        
    
# Initializing the layout of the app
master = CTk()
master.title("YouTube Downloader")
master.grid_rowconfigure((0,1), weight=1)
master.grid_columnconfigure((0,1), weight=1)
master.geometry("350x150")
master.resizable(False, False)
CTkLabel(master, text="Enter YouTube video URL:").grid(row=0, column=0)
entry = CTkEntry(master)
entry.grid(row=0, column=1)
CTkButton(master, text='Download', command=lambda *args: download_video(entry.get())).grid(row=1, column=0, columnspan=2)
master.mainloop()
