from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__("turtle")
        self.penup()
        self.color("black")
        self.goto(x=0, y=-280)
        self.setheading(90)

    def up(self):
        self.forward(10)

    def down(self):
        self.backward(10)
