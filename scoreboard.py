from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(0, 280)
        self.level = 0
        self.levelup()

    def levelup(self):
        self.clear()
        self.level += 1
        self.write(arg=f"Level: {self.level}", move=False, align="center", font=("Courier", 14, "normal"))

    def lost(self):
        self.goto(0,0)
        self.write("You lost!", move=False, align="center", font=("Courier", 14, "normal"))
