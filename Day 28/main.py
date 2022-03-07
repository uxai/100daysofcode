from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Fira Sans"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
clock = None

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer(min=25):
    time = 60 * min
    count_down(time)

def reset_timer():
    global reps
    reps = 0
    window.after_cancel(clock)
    canvas.itemconfig(timer_text, text="25:00")
    check.config(text="")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global reps
    minutes = math.floor(count / 60)
    seconds = count % 60
    if minutes < 10:
        minutes = f"0{minutes}"
    if seconds < 10:
        seconds = f"0{seconds}"
    display = f"{minutes}:{seconds}"
    canvas.itemconfig(timer_text, text=display)
    if count > 0:
        global clock
        clock = window.after(1000, count_down, count - 1)
    else:
        if reps < 8:
            if reps % 2 == 0:
                reps += 1
                title.config(text="Work time", fg=GREEN)
                start_timer()
            else:
                reps += 1
                title.config(text="Break time", fg=PINK)
                mark = ""
                for _ in range(0, reps, 2):
                    mark += "✔"
                check.config(text=mark)
                start_timer(5)
        else:
            if reps <= 8:
                reps += 1
                title.config(text="Break time", fg=RED)
                start_timer(20)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title = Label(text="Work time", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30))
title.grid(row=0, column=1)

canvas = Canvas(width="200", height="224", bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))
canvas.grid(row=1, column=1)
start_btn = Button(text="Start", bg=RED, fg="#FFFFFF", font=(FONT_NAME, 12, "bold"), highlightthickness=0, command=start_timer)
start_btn.grid(row=2, column=0)

end_btn = Button(text="Reset", bg=RED, fg="#FFFFFF", font=(FONT_NAME, 12, "bold"), highlightthickness=0, command=reset_timer)
end_btn.grid(row=2, column=2)

check = Label(bg=YELLOW, fg="#9ba440", font=(FONT_NAME, 15))
check.grid(row=3, column=1)

window.mainloop()