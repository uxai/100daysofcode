from tkinter import *
from tkinter import messagebox
from password_generator import password_generator
import pyperclip

FONT_STYLE = ("Fira Sans", 11)
BACKGROUND = "#08111B"
INPUT_BG = "#151E28"
TEXT = "#FFFFFF"

def random_pswd():
    new_password = password_generator()
    password_entry.insert(0, new_password)
    pyperclip.copy(new_password)

def save_pswd():

    app = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(app) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Incomplete details", message="Please make sure to fill in all the form details before saving!")
    else:
    
        is_okay = messagebox.askokcancel(title=app, message=f"Would you like to save the details: \nEmail: {email}\nPassword: {password}\n Is it okay to save?")

        if is_okay:
            with open("passwords.txt", "a") as file:
                file.write(f"{app}, {email}, {password}\n")

            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()



window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40, bg=BACKGROUND)

for row in range(1, 5):
    window.grid_rowconfigure(row, minsize=40)

lock = PhotoImage(file="logo.png")
lock = lock.subsample(2, 2)

canvas = Canvas(width="420", height="170", highlightthickness=0, bg=BACKGROUND)
canvas.create_image(210, 85, image=lock)
canvas.grid(row=0, column=0, columnspan=4)

website_label = Label(text="Service Name: ", font=FONT_STYLE, bg=BACKGROUND, fg=TEXT)
website_label.grid(row=1, column=1, sticky="E")

website_entry = Entry(width=36, font=FONT_STYLE, bg=INPUT_BG, fg=TEXT, insertbackground=TEXT)
website_entry.grid(row=1, column=2, columnspan=2, sticky="W", ipadx=5, ipady=5)
website_entry.focus()

email_label = Label(text="Username: ", font=FONT_STYLE, bg=BACKGROUND, fg=TEXT)
email_label.grid(row=2, column=1, sticky="E")

email_entry = Entry(width=36, font=FONT_STYLE, bg=INPUT_BG, fg=TEXT, insertbackground=TEXT)
email_entry.grid(row=2, column=2, columnspan=2, sticky="W", ipadx=5, ipady=5)
email_entry.insert(0, "matt.talebi@live.com")

password_label = Label(text="Password: ", font=FONT_STYLE, bg=BACKGROUND, fg=TEXT)
password_label.grid(row=3, column=1, sticky="E")

password_entry = Entry(width=18, font=FONT_STYLE, bg=INPUT_BG, fg=TEXT, insertbackground=TEXT)
password_entry.grid(row=3, column=2,  sticky="W", ipadx=5, ipady=5)

generate_pass = Button(text="Generate Password", bg="#F4477B", fg=TEXT, font=FONT_STYLE, command=random_pswd)
generate_pass.grid(row=3, column=3, sticky="E")

save_btn = Button(text="Save Credentials", width=36, bg="#22C27F", fg="#0B472E", font=FONT_STYLE, command=save_pswd)
save_btn.grid(row=4, column=2, columnspan=2)

window.mainloop()