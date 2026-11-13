import tkinter as tk
import random

colours = ["turquoise", "light blue", "yellow", "pink", "coral"]

counter = 1

def does_a_thing():
    global counter
    counter += 1
    my_second_button.configure(bg=random.choice(colours), text=counter)

win = tk.Tk()
win.title("My window")
win.geometry("400x300")
my_first_button = tk.Button(win,text="Press me",bg="red",fg="hot pink", command=does_a_thing)
my_second_button = tk.Button(win,text="Not me",bg="yellow",fg="blue")

win.rowconfigure(index=0, weight=1)
#win.rowconfigure(index=1, weight=1)
win.columnconfigure(index=0, weight=1)
win.columnconfigure(index=1, weight=1)

my_first_button.grid(sticky="", row=0)
my_second_button.grid(sticky="news", row=0, column=1)
win.mainloop()
