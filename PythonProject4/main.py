import tkinter
from tkinter import *
window = tkinter.Tk()
window.title("my first tkinter window")


window.minsize(500, 300)
# my lable
my_label = tkinter.Label(text="my first tkinter window", font=("Arial", 18), fg="black")
my_label.pack(side="bottom")

my_label["text"]= "my  tkinter window"
my_label.config(text="my tkinter window")
lable = tkinter.Label(text="my first tkinter window", font=("Arial", 18), fg="black")
# button adding

def button_clicked():

    my_label.pack(side="top")
    new_text = input.get()
    my_label.config(text=f"you spanked me {new_text}")



button = Button(text="click", command=button_clicked)

button.pack(side = "bottom")
# entry


input = Entry(width=20, )
input.pack(side = "bottom")
print(input.get())
















window.mainloop()

