# Turbo RAM Downloader
#
# A joke program for downloading RAM from Internet
# Inspired by Download More RAM! website [https://downloadmoreram.com]
# Written in Python 3.10.5
#
# Copyright (c) Ivan Movchan, 2022
# [https://github.com/NobootRecord]

from tkinter import * # Using Tkinter as GUI framework
from tkinter import messagebox as msgbox # Also import tkinter.messagebox
from time import sleep # Using time for sleeping
import webbrowser # Using webbrowser for opening URLs
from random import * # Using random for random number generating

# RAM downloading function
def ram_download():
    if l.get(ANCHOR) == '':
        msgbox.showerror(message='Select the RAM downloading plan first!', title='Error')
    else:
        for i in range(0, 101):
            print('Downloading RAM... ', i, end='% completed\t\r')
            sleep(randint(0, 9000) / 100000)
        print('Extracting and installing RAM, please wait...', end='\r')
        sleep(1337 / 100)
        print('Done.', end='\t\t\t\t\t\t\r')
        msgbox.showinfo(message='Successfully downloaded RAM!\nThank you very much for using Turbo RAM Downloader!!1', title='Done')


# Online help
def online_help():
    webbrowser.open('https://youtube.com/watch?v=dQw4w9WgXcQ')

# About
def about_program():
    msgbox.showinfo(title='About...', message='Version 0.236943584323 build 0347205\nCoded by Ivan Movchan aka NobootRecord\nCopyright/Pasteleft (c) 2022\n\nInspired by [https://downloadmoreram.com] website :-)')

# GitHub
def fork_github():
    webbrowser.open('https://github.com/NobootRecord/TurboRAMDownloader')

# Initialize main window
g = Tk()
g.title('Turbo RAM Downloader')
g.geometry('320x320')

# Add listbox
l = Listbox()
l.insert(END, '4 GB')
l.insert(END, '8 GB')
l.insert(END, '16 GB')
l.insert(END, '32 GB')
l.grid()

# Add buttons
b1 = Button(text='Download!', command=ram_download)
b1.grid()
b2 = Button(text='Online help', command=online_help)
b2.grid()
b3 = Button(text='About...', command=about_program)
b3.grid()
b4 = Button(text='Fork me on GitHub lol', command=fork_github)
b4.grid()

print('Ready.', end='\r') # Ready to go...
g.mainloop() # Let's go!!!
