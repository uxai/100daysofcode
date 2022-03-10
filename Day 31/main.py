from tkinter import *
import csv
import random
import time

BACKGROUND_COLOR = "#B1E1BE"
current_word = ""
vocabulary = {}

def remove_word():
    if current_word:
        vocabulary.pop(current_word)
    get_word()

def get_word():
    current_word = random.choice(list(vocabulary))
    card.itemconfigure(language, text="French")
    card.itemconfigure(word, text=current_word)
    window.after(3000, get_translation, vocabulary[current_word])
    

def get_translation(translated):
    card.itemconfigure(language, text="English")
    card.itemconfigure(word, text=translated)

with open("data/french_words.csv", "r", encoding="utf-8") as file:
    csv = csv.reader(file)
    for line in csv:
        vocabulary[line[0]] = line[1]


window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

correct = PhotoImage(file="images/right.png")
correct = correct.subsample(2, 2)

incorrect = PhotoImage(file="images/wrong.png")
incorrect = incorrect.subsample(2, 2)

card = Canvas(window, height=240, width=400, bg="#FFFFFF", highlightthickness=0)
card.grid(row=0, column=0, columnspan=2)

language = card.create_text(200, 100, text= "Ready?",width=400,fill="black",font=("fira sans", 15), justify="center")
word = card.create_text(200, 150, text= "Click the green check to start!",width=400,fill="black",font=("fira sans bold", 20), justify="center")

# french = Label(card, text="Hello World.", bg="#FFFFFF")
# french.grid(row=0, column=0)

wrong_btn = Button(image=incorrect, highlightthickness=0, borderwidth=0, command=get_word)
wrong_btn.grid(row=1, column=0, sticky="W")

right_btn = Button(image=correct, highlightthickness=0, borderwidth=0, command=remove_word)
right_btn.grid(row=1, column=1, sticky="E")

window.mainloop()
