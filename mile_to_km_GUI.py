# GUI
from tkinter import *

FONT = ("Consolas", 14, "normal")


def button_clicked():
    ans = float(entry.get())
    ans *= 1.609
    lab3.config(text=f"{round(ans)}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=50, pady=50)

entry = Entry(width=10)
entry.grid(column=1, row=0)

lab1 = Label(text="Miles", font=FONT)
lab1.grid(column=2, row=0)

lab2 = Label(text="is equal to", font=FONT)
lab2.grid(column=0, row=1)

lab3 = Label(text="0", font=FONT)
lab3.grid(column=1, row=1)

lab4 = Label(text="Km", font=FONT)
lab4.grid(column=2, row=1)

button = Button(text="Calculate", font=FONT, command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
