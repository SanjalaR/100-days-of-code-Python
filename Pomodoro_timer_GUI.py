# Pomodoro Timer
import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checks = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_click():
    global checks, reps, timer
    checks = ""
    reps = 0
    window.after_cancel(timer)
    lab1.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_click():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        lab1.config(text="Break", fg=RED)
        count(long_sec)
    elif reps % 2 == 0:
        lab1.config(text="Break", fg=PINK)
        count(short_sec)
    else:
        lab1.config(text="Work", fg=GREEN)
        count(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count(number):
    global checks, timer
    count_min = math.floor(number / 60)
    count_sec = int(number % 60)
    if count_sec <= 9:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if number > 0:
        timer = window.after(1000, count, number - 1)
    else:
        start_click()
        if reps % 2 == 0:
            checks += "✔"
            lab2.config(text=checks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

lab1 = Label(text="Timer", font=(FONT_NAME, 50, "normal"), fg=GREEN, bg=YELLOW)
lab1.grid(column=1, row=0)

lab2 = Label(fg=GREEN, bg=YELLOW)
lab2.grid(column=1, row=3)

but1 = Button(text="Start", font=(FONT_NAME, 14, "normal"), highlightthickness=0, command=start_click)
but1.grid(column=0, row=2)

but2 = Button(text="Reset", font=(FONT_NAME, 14, "normal"), highlightthickness=0, command=reset_click)
but2.grid(column=2, row=2)

window.mainloop()
