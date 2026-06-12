from tkinter import *


def milesToKilometers():
    mile = miles_input.get()
    mile = float(mile)
    km = mile * 1.60934
    kilometer.config(text=f"{km}")


window = Tk()
window.title("Mile to Kilometer")
window.config(padx=20, pady=20)

miles_input = Entry(width=6)
miles_input.grid(row=1, column=0)

miles = Label(text="Miles")
miles.grid(row=2, column=0)
is_equal = Label(text="is equal to")
is_equal.grid(row=0, column=1)

kilometer_result = Label(text="0")
kilometer_result.grid(row=1, column=1)

kilometer = Label(text="kilometers")
kilometer.grid(row=2, column=1)


calc_buttton = Button( text="Calculate", command=milesToKilometers)
calc_buttton.grid(row=1, column=2)















window.mainloop()
