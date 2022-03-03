import tkinter as tk

def convert():
    mi = float(miles_in.get())
    km = mi * 1.6
    kilometer_converted.config(text=f"{km:.2f}")

window = tk.Tk()
window.title("Miles to Kilometer")
window.minsize(width=300, height=200)
window.config(padx=20, pady=20)

miles_in = tk.Entry()
miles_in.grid(row=0, column=1)

miles_label = tk.Label(text="Miles", font=("Fira Sans", 12))
miles_label.grid(row=0, column=2)
miles_label.config(padx=5, pady=5)

is_equal_label = tk.Label(text="is equal to", font=("Fira Sans", 12))
is_equal_label.grid(row=1, column=0)
is_equal_label = tk.Label(text="is equal to", font=("Fira Sans", 12))
is_equal_label.grid(row=1, column=0)
kilometer_converted = tk.Label(text="", font=("Fira Sans", 12))
kilometer_converted.grid(row=1, column=1)
kilometer_label = tk.Label(text="Kilometers", font=("Fira Sans", 12))
kilometer_label.grid(row=1, column=2)

button = tk.Button(text="Convert", command=convert)
button.grid(row=2, column=1)




window.mainloop()