from tkinter import *
import pandas
import random
from tkinter import messagebox

BACKGROUND_COLOR = "#2596be"
TITLE = ("Ariel", 40, "italic")
WORD = ("Ariel", 60, "bold")

ok = messagebox.askquestion(title="I'll let you choose", message="Do you want to revise the whole thing?")

if ok:
    data = pandas.read_csv("data/original.csv")
    print("Revise")
else:
    try:
        data = pandas.read_csv("data/to_learn.csv")
        print("Learn")
    except FileNotFoundError:
        data = pandas.read_csv("data/Untitled spreadsheet - Sheet1.csv")
        print("Start")

data = data.to_dict(orient="records")
print(data)

new_word = {}


# ---------------------------- FLIP CARD ------------------------------- #
def know():
    data.remove(new_word)
    new_card()
    to_learn = pandas.DataFrame(data)
    to_learn.to_csv("data/to_learn.csv", index=False)


# ---------------------------- FLIP CARD ------------------------------- #
def flip():
    global new_word
    canvas.itemconfig(lang, text="English", fill="white")
    canvas.itemconfig(word, text=new_word["English"], fill="white")
    canvas.itemconfig(img, image=back)


# ---------------------------- NEW CARD ------------------------------- #
def new_card():
    global new_word, flip_timer
    window.after_cancel(flip_timer)
    new_word = random.choice(data)
    canvas.itemconfig(lang, text="German", fill="black")
    canvas.itemconfig(word, text=new_word["German"], fill="black")
    canvas.itemconfig(img, image=front)
    flip_timer = window.after(3000, func=flip)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, func=flip)

front = PhotoImage(file="images/card_front.png")
back = PhotoImage(file="images/card_back.png")
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
img = canvas.create_image(400, 250, image=front)
lang = canvas.create_text(400, 150, text="Title", font=TITLE)
word = canvas.create_text(400, 263, text="word", font=WORD)
canvas.grid(column=0, row=0, columnspan=2)

but1 = Button(image=right, highlightthickness=0, command=know)
but1.grid(column=1, row=1)

but2 = Button(image=wrong, highlightthickness=0, command=new_card)
but2.grid(column=0, row=1)

new_card()

window.mainloop()
