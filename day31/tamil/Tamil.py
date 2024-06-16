from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
TITLE = ("Ariel", 40, "italic")
WORD = ("Ariel", 60, "bold")

try:
    data = pandas.read_csv("data/to_learn.csv")
except FileNotFoundError:
    ori_data = pandas.read_csv("data/Untitled spreadsheet - Sheet1.csv")
    data = ori_data.to_dict(orient="records")
else:
    data = data.to_dict(orient="records")
new_word = {}


# ---------------------------- NEW CARD ------------------------------- #
def know():
    data.remove(new_word)
    new_card()
    to_learn = pandas.DataFrame(data)
    to_learn.to_csv("data/to_learn.csv", index=False)


# ---------------------------- NEW CARD ------------------------------- #
def flip():
    global new_word
    canvas.itemconfig(img, image=back)
    canvas.itemconfig(lang, text="English")
    canvas.itemconfig(word, text=new_word["English"])


# ---------------------------- NEW CARD ------------------------------- #
def new_card():
    global new_word, flip_timer
    window.after_cancel(flip_timer)
    new_word = random.choice(data)
    canvas.itemconfig(img, image=front)
    canvas.itemconfig(lang, text="Tamil")
    canvas.itemconfig(word, text=new_word["Tamil"])
    flip_timer = window.after(3000, func=flip)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, func=flip)

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)

front = PhotoImage(file="images/card_front.png")
back = PhotoImage(file="images/card_back.png")
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")

img = canvas.create_image(400, 263, image=front)

lang = canvas.create_text(400, 150, text="Title", font=TITLE)
word = canvas.create_text(400, 263, text="word", font=WORD)

canvas.grid(column=0, row=0, columnspan=2)

but1 = Button(image=right, highlightthickness=0, command=know)
but1.grid(column=1, row=1)
but2 = Button(image=wrong, highlightthickness=0, command=new_card)
but2.grid(column=0, row=1)

new_card()

window.mainloop()
