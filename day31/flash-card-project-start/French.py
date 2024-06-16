from tkinter import *
import random
import pandas
import time

BACKGROUND_COLOR = "#B1DDC6"
TITLE = ("Ariel", 40, "italic")
WORD = ("Ariel", 60, "bold")
data_dict = {}
new_word = {}

# ---------------------------- CREATE FLASH CARDS ------------------------------- #
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    ori_data = pandas.read_csv("data/french_words.csv")
    data_dict = ori_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")
print(data_dict)



def know():
    data_dict.remove(new_word)
    new_card()
    to_learn = pandas.DataFrame(data_dict)
    to_learn.to_csv("data/words_to_learn.csv", index=False)


def new_card():
    global new_word, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(lang, text="French", fill="black")
    new_word = random.choice(data_dict)
    canvas.itemconfig(word, text=new_word["French"], fill="black")
    canvas.itemconfig(img, image=front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    global new_word
    canvas.itemconfig(img, image=back)
    canvas.itemconfig(lang, text="English", fill="white")
    canvas.itemconfig(word, text=new_word["English"], fill="white")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
front = PhotoImage(file="./images/card_front.png")
back = PhotoImage(file="images/card_back.png")
img = canvas.create_image(400, 263, image=front)
canvas.config(highlightthickness=0, background=BACKGROUND_COLOR)
lang = canvas.create_text(400, 150, text="Title", font=TITLE)
word = canvas.create_text(400, 263, text="word", font=WORD)
canvas.grid(column=0, row=0, columnspan=2)

wrong = PhotoImage(file="./images/wrong.png")
but1 = Button(image=wrong, highlightthickness=0, command=new_card)
but1.grid(column=0, row=1)

right = PhotoImage(file="./images/right.png")
but2 = Button(image=right, highlightthickness=0, command=know)
but2.grid(column=1, row=1)

new_card()

window.mainloop()
