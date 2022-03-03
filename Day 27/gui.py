import tkinter as tk

window = tk.Tk()
window.title("My Program")
window.minsize(width=800, height=600)
window.config(padx=20, pady=20)

# Label
my_label = tk.Label(text="Input your name", font=("Fira Sans", 24))
# Place into the screen and automatically center it.
# Expand takes whole screen, text is centered in label
my_label.grid(row=0, column=0)
my_label.config(padx=20, pady=20)

# Button
def button_clicked():
    my_label.config(text=f"Welcome {input.get()}!")

# Entry
input = tk.Entry()
input.grid(row=4, column=4)

button = tk.Button(text="Submit", command=button_clicked)
button.grid(row=1, column=1)

button2 = tk.Button(text="Reset", command=button_clicked)
button2.grid(row=0, column=2)

window.mainloop()
