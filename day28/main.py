import math
import tkinter
from idlelib import window
from pydoc import text
from tkinter import *

import timer

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    works_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="break", fg=RED , bg=YELLOW)
    elif reps %2  == 0:
        count_down(short_break_sec)
        label.config(text="break", fg=PINK, bg=YELLOW)
    else:
        count_down(works_sec)
        label.config(text="break", fg=GREEN, bg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"


    canvas.itemconfig(timer_text,text= f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_mark.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window =Tk()
window.title("pomodorom")
window.config(padx=100, pady=50, bg=YELLOW)


label =Label(text="TIMER", fg=GREEN , bg=YELLOW ,font=(FONT_NAME,20,"bold"))

label.grid(column=1, row=0)





canvas = Canvas(window, width=200, height=224,bg=YELLOW , highlightthickness=0)
tomato_pic = PhotoImage(file="tomato.png")
canvas.create_image(100,108, image=tomato_pic)
timer_text = canvas.create_text(100,126, text= "00:00",font=(FONT_NAME, 40, "bold"))
canvas.grid(column=1, row=1)




start_button = Button(text="start", highlightthickness=0,command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="reset" , highlightthickness=0,command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark = Label(text="✅" , fg=GREEN, bg= YELLOW ,font=(FONT_NAME, 10, "bold") )
check_mark.grid(column=1, row=3)

window.mainloop()