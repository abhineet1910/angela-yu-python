from tkinter import *
from tkinter import messagebox

import pandas as pd
from random import *

try:
    df = pd.read_csv("data/words_to_learn.csv")
    # record : list like [{column-->value},,,,{column___>value}]
except FileNotFoundError:
    orignal_data = pd.read_csv("data/french_words.csv")
    dataframe = orignal_data.to_dict("records")
else:
    dataframe = df.to_dict(orient="records")
# print(dataframe)

def randomfrench_word():
    global new_word,flip_timmer
    window.after_cancel(flip_timmer)
    new_word = choice(dataframe)
    canvas.itemconfig(card_title, text="French",fill="black")
    canvas.itemconfig(card_word, text=new_word["French"],fill="black")
    canvas.itemconfig(canvas_image,image= front_img)
    flip_timmer = window.after(3000,func=flip_card)

    # earlier i was trying to do with this but now i reduce the code to more simple one
    # global french
    # french = new_word["French"]
    # global english
    # english = new_word["English"]
    #
    # french_lable = Label(text="french", bg="white")
    # french_lable.config(font=("Arial", 40, "italic"))
    # french_lable.place(x=330, y=150)
    #
    # frenchletter_lable = Label(text=french, bg="white")
    # frenchletter_lable.config(font=(english, 60, "bold"))
    # frenchletter_lable.place(x=280, y=265)


def flip_card():
    global new_word
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=new_word["English"],fill="white")
    canvas.itemconfig(canvas_image,image= back_img)


def is_known():
    dataframe.remove(new_word)
    randomfrench_word()
    # to creat new csv file out of exixting file
    data = pd.DataFrame(dataframe)
    # to convert exixting file type to csv file
    data.to_csv("data/words_to_learn.csv",index=False)



BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("FLASHY")
window.config(background=BACKGROUND_COLOR,padx=50,pady=50)

flip_timmer = window.after(3000,func=flip_card)

canvas = Canvas(width=800, height=526)
back_img = PhotoImage(file="images/card_back.png")
front_img = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(410, 260, image=front_img)

canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
card_title = canvas.create_text(400,150,text="title",font=("Arial", 40, "italic"))
card_word = canvas.create_text(400,263,text="word",font=("Arial", 40, "bold"))
canvas.grid(row=0, column=0,columnspan=2)

window.after(3000,func=flip_card)

wrong_logo = PhotoImage(file="images/wrong.png")
right_logo = PhotoImage(file="images/right.png")

wrong_button = Button(image=wrong_logo,highlightthickness=0,command=randomfrench_word)
wrong_button.grid(row=2,column=0)

right_button = Button(image=right_logo,highlightthickness=0,command=is_known)
right_button.grid(row=2,column=1)




randomfrench_word()



















window.mainloop()
