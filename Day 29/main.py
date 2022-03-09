from tkinter import *
from tkinter import messagebox
from password_generator import password_generator
import pyperclip
import json

FONT_STYLE = ("Fira Sans", 11)
LABEL_STYLE = ("Fira Sans", 8)
BACKGROUND = "#08111B"
INPUT_BG = "#151E28"
TEXT = "#FFFFFF"

def mask_pswd():
    if var1.get() == 1:
        password_entry.config(show="")
        verifypw_entry.config(show="")
    else:
        password_entry.config(show="*")
        verifypw_entry.config(show="*")

def random_pswd():
    new_password = password_generator()
    password_entry.delete(0, END)
    verifypw_entry.delete(0, END)
    password_entry.insert(0, new_password)
    verifypw_entry.insert(0, new_password)
    pyperclip.copy(new_password)

def search_pswd():
    app = website_entry.get()
    try:
        with open("passwords.json", "r") as file:
            retreival = json.load(file)
            print(retreival[app])
            messagebox.showinfo(title=app, message=f"Username: {retreival[app]['email']}\nPassword has been copied to your clipboard.")
            pyperclip.copy(retreival[app]['password'])

    except FileNotFoundError:
        print("File unreadable")
    except KeyError:
        print("Key error")  


# SAVE PASSWORD TO JSON
def save_pswd():

    app = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    verify = verifypw_entry.get()

    if password == verify:
        new_data = {
            app: {
                "email": email,
                "password": password
            }
        }

        if len(app) == 0 or len(email) == 0 or len(password) == 0:
            messagebox.showerror(title="Incomplete details", message="Please make sure to fill in all the form details before saving!")
        else:
            try:
                with open("passwords.json", "r") as data_file:
                    data = json.load(data_file)
                    data.update(new_data)
            except:
                data = new_data

            with open("passwords.json", "w") as data_file:
                data.update(new_data)
                json.dump(data, data_file, indent=4)
            print(data)

            website_entry.delete(0, END)
            password_entry.delete(0, END)
            verifypw_entry.delete(0, END)
            website_entry.focus()
    else:
        messagebox.showerror(title="Passwords don't match", message="Please make sure your verified password matches before saving.")



# BUILD UI FOR APPLICATION
window = Tk()
window.iconbitmap('images/icon.ico')
window.title("Password Manager")
window.config(padx=60, pady=40, bg=BACKGROUND)

for row in range(1, 5):
    window.grid_rowconfigure(row, minsize=40)


lock = PhotoImage(file="images/logo.png")
lock = lock.subsample(2, 2)

canvas = Canvas(width="420", height="170", highlightthickness=0, bg=BACKGROUND)
canvas.create_image(210, 85, image=lock)
canvas.grid(row=0, column=0, columnspan=4)

website_label = Label(text="Service Name: ", font=FONT_STYLE, bg=BACKGROUND, fg=TEXT)
website_label.grid(row=1, column=0, sticky="E")

website_entry = Entry(font=FONT_STYLE, bg=INPUT_BG, fg=TEXT, insertbackground=TEXT)
website_entry.grid(row=1, column=1, columnspan=2, sticky="WE", ipadx=5, ipady=5, padx=5, pady=5)
website_entry.focus()

search_btn = Button(text="Search", bg="#F4477B", fg=TEXT, font=FONT_STYLE, command=search_pswd)
search_btn.grid(row=1, column=3, sticky="WE", padx=5, pady=5)

email_label = Label(text="Username: ", font=FONT_STYLE, bg=BACKGROUND, fg=TEXT)
email_label.grid(row=2, column=0, sticky="E")

email_entry = Entry(font=FONT_STYLE, bg=INPUT_BG, fg=TEXT, insertbackground=TEXT)
email_entry.grid(row=2, column=1, columnspan=3, sticky="WE", ipadx=5, ipady=5, padx=5, pady=5)
email_entry.insert(0, "matt.talebi@live.com")

password_label = Label(text="Password: ", font=FONT_STYLE, bg=BACKGROUND, fg=TEXT)
password_label.grid(row=3, column=0, sticky="E")

password_entry = Entry(font=FONT_STYLE, show="*", bg=INPUT_BG, fg=TEXT, insertbackground=TEXT)
password_entry.grid(row=3, column=1,  sticky="WE", ipadx=5, ipady=5, padx=5, pady=5)

newpw_label = Label(text="New Password", font=LABEL_STYLE, bg=BACKGROUND, fg="#6D8197")
newpw_label.grid(row=4, column=1, sticky="NW")

verify_label = Label(text="Verify Password", font=LABEL_STYLE, bg=BACKGROUND, fg="#6D8197")
verify_label.grid(row=4, column=2, sticky="NW")

verifypw_entry = Entry(font=FONT_STYLE, show="*", bg=INPUT_BG, fg=TEXT, insertbackground=TEXT)
verifypw_entry.grid(row=3, column=2,  sticky="WE", ipadx=5, ipady=5, padx=5, pady=5)

generate_pass = Button(text="Generate Password", bg="#F4477B", fg=TEXT, font=FONT_STYLE, command=random_pswd)
generate_pass.grid(row=3, column=3, sticky="WE", padx=5, pady=5)

var1 = IntVar()
show_pass = Checkbutton(window, text="Show password", variable=var1, onvalue=1, offvalue=0,  command=mask_pswd, bg=BACKGROUND, font=FONT_STYLE, fg="#FFFFFF", selectcolor="black", activebackground=BACKGROUND, activeforeground="#FFFFFF")
show_pass.grid(row=5, column=1, sticky="NW")

save_btn = Button(text="Save Credentials", width=36, bg="#22C27F", fg="#0B472E", font=FONT_STYLE, command=save_pswd)
save_btn.grid(row=6, column=1, columnspan=2, sticky="WE")

window.mainloop()