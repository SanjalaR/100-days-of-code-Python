#Draw a random walk using turtle graphics
import turtle
from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("plum")

import random

timmy.pensize(10)
timmy.speed(10)


def right():
    timmy.right(90)
    timmy.forward(30)
    print("Right")


def left():
    timmy.left(90)
    timmy.forward(30)
    print("Left")


def straight():
    timmy.forward(30)
    print("Straight")


def back():
    timmy.backward(30)
    print("Back")


turtle.colormode(255)

# colors = ["deep pink", "purple", "yellow", "red", "orange", "spring green", "medium blue", "magenta"]
motion = [straight, right, left, back]
for i in range(200):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_tuple = (r, g, b)
    timmy.color(my_tuple)
    random.choice(motion)() 

screen = Screen()
screen.exitonclick()
