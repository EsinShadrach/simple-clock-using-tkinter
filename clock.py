from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)
label = Label(root, font = ("ds-digitale", 60),background = "white", foreground = "blue")
label.pack(anchor = 'center')
button = Button (root,text = "close", command = quit).pack()
time()

mainloop()
