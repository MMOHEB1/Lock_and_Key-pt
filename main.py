from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pswrd_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website1 = website_input.get()
    email1 = email_input.get()
    pswrd1 = pswrd_input.get()
    new_data = {
        website1: {
            "Email": email1,
            "Password": pswrd1
        }
    }

    if len(website1) == 0 or len(pswrd1) == 0:
        messagebox.showinfo(title="OOP", message="Please do not leave any fields empty")
    else:
        with open("data.json", "r") as security_file:
            # Reading old data
            data = json.load(security_file)
            # Updating old data with new data
            data.update(new_data)

        with open("data.json", "w") as security_file:
            # Dumping/saving data into data file
            json.dump(data, security_file, indent=4)

            # deletes the inputs of the website and password once add is clicked
            website_input.delete(0, END)
            pswrd_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(pady=20, padx=20)
window.title("Password Manager")
img_file = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=img_file)
canvas.grid(column=1, row=0)

# Website label:
website = Label(text="Website:")
website.grid(column=0, row=1)

website_input = Entry(window)
website_input.grid(column=1, row=1, columnspan=2, sticky='nsew')
website_input.focus()

# Email label:
email = Label(text="Email/Username:")
email.grid(column=0, row=2)

email_input = Entry(window)
email_input.grid(column=1, row=2, columnspan=2, sticky='nsew')
email_input.insert(0, "mohebimustafa99@gmail.com")

# Password label:
pswrd = Label(text="Password:")
pswrd.grid(column=0, row=3)

pswrd_input = Entry(window)
pswrd_input.grid(column=1, row=3, sticky='nsew')

# Buttons:
generate_pswrd = Button(text="Generate Password", command=generate_password)
generate_pswrd.grid(column=2, row=3)

add = Button(text="Add", command=save)
add.grid(column=0, row=4, columnspan=3, sticky='nsew')

window.mainloop()
