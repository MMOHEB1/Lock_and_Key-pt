from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website1 = website_input.get()
    email1 = email_input.get()
    pswrd1 = pswrd_input.get()

    messagebox.showinfo(title="title, message="hello")

    with open("data.txt", "a") as security_file:
        security_file.write(f"\n {website1} | {email1} | {pswrd1}\n")
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

generate_pswrd = Button(text="Generate Password")
generate_pswrd.grid(column=2, row=3)

# button_perss:
add = Button(text="Add", command=save)
add.grid(column=0, row=4, columnspan=3, sticky='nsew')







window.mainloop()