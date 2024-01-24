import turtle
from turtle import Turtle
import random

COLORS = [(236, 35, 108), (145, 28, 66), (239, 75, 36), (7, 148, 95), (222, 170, 45), (183, 158, 47),
          (44, 191, 232), (28, 127, 194), (254, 223, 0), (125, 192, 78), (85, 27, 92), (244, 219, 53),
          (178, 40, 98), (40, 168, 117), (208, 131, 165), (205, 56, 35), (239, 162, 194), (147, 26, 24),
          (242, 168, 158), (162, 211, 178), (140, 211, 232), (7, 115, 55), (26, 186, 225), (84, 133, 177),
          (163, 193, 227), (112, 9, 8)]


class Car:
    def __init__(self):
        self.list = []
        self.move = 5

    def create(self):
        if random.randint(1,6) == 1:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            turtle.colormode(255)
            car.color(random.choice(COLORS))
            y = random.randint(-250, 250)
            car.penup()
            car.goto(300, y)
            self.list.append(car)

    def start(self):
        for car in self.list:
            car.backward(self.move)

    def increase(self):
        self.move += 10
