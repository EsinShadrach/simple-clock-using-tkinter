from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock")
date = strftime('%h-%d-%Y')

def time():
    string = strftime('%I:%M:%S %p')
    time_.config(text=string)
    time_.after(1000, time)



date_ = Label(
    root, font = ("ds-digitale", 67),
        background = "black",
        text = date,
        foreground = '#fa8072'
    )

time_ = Label(
    root, font = ("ds-digitale", 68),
        background = "black",
        foreground= "coral"
    )


date_.pack(
    anchor = "center"
    )
time_.pack(
    anchor = "center"
    )

time()
mainloop()
