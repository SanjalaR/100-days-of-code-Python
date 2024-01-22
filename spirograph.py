#Draw a spirograph using turtle graphics
import turtle
from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("plum")

import random

turtle.colormode(255)
timmy.speed("fastest")
angle = 5
for i in range(int(360/angle)):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_tuple = (r, g, b)
    timmy.color(my_tuple)
    timmy.circle(100)
    timmy.left(angle)

screen = Screen()
screen.exitonclick()
