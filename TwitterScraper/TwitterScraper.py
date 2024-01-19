import os
import csv
from tkinter import *
import tkinter as tk
from tkinter import Radiobutton, ACTIVE, DISABLED

# Window
root = Tk()
root.title("Twitter Scraper")
root.geometry('300x300+500+200')

# Sub-Routines
# Scrape
def scrape():
    if v1.get() == 0:
        if v2.get() == 0:
            os.system("start twint -u "+user.get()+" -o "+user.get()+".csv --csv")
        elif v2.get() == 1:
            os.system("start twint -u"+user.get()+" --followers -o "+user.get()+".csv --csv")
        else:
            os.system("start twint -u" + user.get() + " --following -o " + user.get() + ".csv --csv")
    else:
        os.system("start twint -s "+user.get()+" -o "+user.get()+".csv --csv")

# Open
def open():
    os.system('start '+os.path.join(os.getcwd(),user.get())+'.csv')
# Enable
def enable():
    full.config(state=ACTIVE)
    followers.config(state=ACTIVE)
    following.config(state=ACTIVE)
# Disable
def disable():
    full.config(state=DISABLED)
    followers.config(state=DISABLED)
    following.config(state=DISABLED)

# Dummy
def dummy():
    pass

# Label
title = Label(root, text = "Twitter Scraper", font=("Consolas", 14), anchor=CENTER, width=30).grid(row = 0, column = 0)

# Frame
main = Frame(root)
main.grid(row =1, column=0)

# Variables
v1 = tk.IntVar()
v1.set(0)
v2 = tk.IntVar()
v2.set(0)
s = tk.StringVar()
s.set("normal")

# Label - Input
inputLabel = Label(main, text="Enter the username\hashtag below", font=("Consolas", 10)).grid(row = 0, column = 0)

# Input Box
user = Entry(main, width = 20, bg = "light grey")
user.grid(row = 1, column = 0)

# Label - Option
option = Label(main, text="Select query type", font=("Consolas", 10)).grid(row = 2, column = 0)

# Buttons
# Radio Buttons
username = Radiobutton(main, variable = v1, value = 0 ,text = "Username", command = enable)
username.grid(row = 3, column = 0)
hashtag = Radiobutton(main, variable = v1, value = 1 ,text = "Hashtag  ", command = disable)
hashtag.grid(row = 4, column = 0)

# Label - Option
option = Label(main, text="Select your parameter", font=("Consolas", 10))
option.grid(row = 5, column = 0)

full =  Radiobutton(main, variable = v2, value = -0 ,text = "Full Data ", command = dummy)
full.grid(row = 6, column = 0)
followers = Radiobutton(main, variable = v2, value = 1 ,text = "Followers", command = dummy)
followers.grid(row = 7, column = 0)
following = Radiobutton(main, variable = v2, value = -1 ,text = "Following", command = dummy)
following.grid(row = 8, column = 0)

# Scrape Button
Button(main, text = "Scrape", width = 20, command = scrape).grid(row = 9, column = 0)
# Open Button
Button(main, text = "Open .csv", width = 20, command = open).grid(row = 10, column = 0)

# End of code
root.mainloop()