# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *

window = Tk()
window.config(pady=20, padx=20)
window.title("Password Manager")
canvas = Canvas(width=200, height=200, highlightthickness=0)
img_file = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img_file)
canvas.pack()






window.mainloop()