import tkinter as tk
import random

colours = ["turquoise", "light blue", "yellow", "pink", "coral"]

counter = 1

def does_a_thing(i, j):
    global counter
    counter += 1

    print(i, j)

win = tk.Tk()
win.title("My window")
win.geometry("400x300")

button_list = []


for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            color = "black"
        else:
            color = "white"
        def special_function(x=i, y=j):
            result_label.configure(text=f"{x}, {y}")
            print(x,y)
        new_button = tk.Button(win,text=f"{i}, {j}",bg=color,fg="grey", command=special_function)

        new_button.grid(sticky="news", row=i, column=j)
        button_list.append((new_button, special_function))
    win.rowconfigure(index=i, weight=1)
    win.columnconfigure(index=i, weight=1)
result_label = tk.Label(win,text="click a cell")
result_label.grid(row=8,columnspan=8)
print(button_list)
win.mainloop()
