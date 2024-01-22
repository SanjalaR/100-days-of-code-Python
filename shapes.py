#Draw 3-10 sided shapes using turtle graphics
import turtle
from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("plum")

import random

colors = ["deep pink", "teal", "purple", "yellow", "red", "orange", "spring green", "medium blue", "magenta"]
for n in range(3, 11):
    i = n
    angle = 360 / n
    while i > 0:
        timmy.color(random.choice(colors))
        timmy.forward(100)
        timmy.right(angle)
        i -= 1

screen = Screen()
screen.exitonclick()
