from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for item in range(nr_letters)]
    password_symbol = [random.choice(symbols) for item in range(nr_symbols)]
    password_number = [random.choice(numbers) for item in range(nr_numbers)]

    password_list = password_letter + password_symbol + password_number


    random.shuffle(password_list)
    password = "".join(password_list)
    # password = ""
    # for char in password_list:
    #   password += char

    entry_password.insert(0, password)
    pyperclip.copy(password)




# ---------------------------- SAVE PASSWORD -


def save():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror("Error", "Please enter all required information")
    else:
        is_ok =messagebox.askokcancel("Password Manager", f"These are the details \nWEBSITE: {website}\nEMAIL: {email}\nPASSWORD: {password}"
                                                              f"do you want to save this")

        if is_ok:
            with open("data.txt","a") as data_file:
                data_file.write(f"{website}|{email}|{password}\n")
                entry_website.delete(0, END)
                entry_email.delete(0, END)
                entry_password.delete(0, END)


# ---------------------------- UI SETUP -------------
# ------------------ #
window = Tk()
window.title("PASSWORD MANAGER")
window.config(padx=20, pady=20,)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

label = Label(text="Website", fg="black",)
label.grid(column=0, row=1)

label_email = Label(text="Email/Username", fg="black",)
label_email.grid(column=0, row=2)

label_password = Label(text="Password", fg="black",)
label_password.grid(column=0, row=3)

entry_website = Entry(width=35)
entry_website.grid(column=1 ,columnspan=2, row=1)
entry_website.focus()


entry_email = Entry(width=35)
entry_email.grid(column=1 ,columnspan=2, row=2)
entry_email.insert(END, "@gmail.com")
entry_email.focus()


entry_password = Entry(width=20)
entry_password.grid(column=1, row=3)
entry_password.focus()


button_generate = Button(text="Generate Password", fg="black",command=generate_password)
button_generate.grid(column=2, row=3)

button_add = Button(text="Add", fg="black",width=36,command=save)
button_add.grid(column=1,columnspan=2, row=4)





window.mainloop()