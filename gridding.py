import tkinter as tk
import random
import time

colours = ["turquoise", "light blue", "yellow", "pink", "coral"]

win = tk.Tk()
win.title("My window")
win.geometry("400x300")

button_list = []

counter = 1
wait = 500
score = 0
current_button = []
lives = 5
started = False

def does_a_thing(i, j):
    global counter
    counter += 1

    print(i, j)

def highlight_button():
    global clicked
    clicked = False
    lost = False
    i = random.randint(0, 7)
    j = random.randint(0, 7)
    button_list[i * 8 + j][0].configure(bg="pink", fg="black")
    global current_button
    current_button = [i, j]
    color = "white" if (i+j) % 2 == 1 else "black"




def start_click():
    global started
    highlight_button()
    start_button.configure(command=lambda:None)
    started = True

def lose():
    win.after(100, win.destroy)

score_label = tk.Label(win, text=f"Score: {score}", bg="grey", fg="black")
score_label.grid(row=8, column=1, columnspan=2)

lives_label = tk.Label(win, text=f"Lives: {"♥"*lives}{"♡︎"*(5-lives)}", bg="grey", fg="black")
lives_label.grid(row=8, column=5, columnspan=3)

start_button = tk.Button(win, text="Start", bg="white", fg="black", command=start_click)
start_button.grid(row=8, columnspan=8)

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            color = "black"
        else:
            color = "white"
        def special_function(x=i, y=j):
            #result_label.configure(text=f"{x}, {y}")
            global score
            global clicked
            global lives
            global started
            if started:
                if [x,y] == current_button:
                    clicked = True
                    color = ("white" if (x+y) % 2 == 1 else "black")
                    button_list[x*8+y][0].configure(bg=color, fg="grey")
                    highlight_button()
                    score += 1
                    score_label.configure(text=f"Score: {score}")
                else:
                    lives -= 1
                    lives_label.configure(text=f"Lives: {"♥"*lives}{"♡"*(5-lives)}")
                    if lives == 0:
                        lose()
        new_button = tk.Button(win,text=f"{i}, {j}",bg=color,fg="grey", command=special_function)

        new_button.grid(sticky="news", row=i, column=j)
        button_list.append((new_button, special_function))
    win.rowconfigure(index=i, weight=1)
    win.columnconfigure(index=i, weight=1)

#result_label = tk.Label(win,text="click a cell")
#result_label.grid(row=8,columnspan=8)
print(button_list)


win.mainloop()

