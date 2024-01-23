from turtle import Turtle, Screen
import time
from day21 import Food, ScoreBoard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


class Snake:
    def __init__(self):
        self.seg = []
        self.create()
        self.head = self.seg[0]

    def create(self):
        for it in range(3):
            t1 = Turtle("square")
            t1.color("white")
            t1.penup()
            t1.goto(x=it * -20, y=0)
            self.seg.append(t1)

    def extend(self):
        t1 = Turtle("square")
        t1.color("white")
        t1.penup()
        t1.goto(self.seg[-1].position())
        self.seg.append(t1)

    def move(self):
        for i in range(len(self.seg) - 1, 0, -1):
            pos = (self.seg[i - 1].xcor(), self.seg[i - 1].ycor())
            self.seg[i].goto(pos)
        self.seg[0].forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)


snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game = True
while game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.change()
        snake.extend()
        scoreboard.clear()
        scoreboard.update()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        game = False
        scoreboard.over()

    # Detect collision with tail
    for segment in snake.seg[1:]:
        if snake.head.distance(segment) < 10:
            game = False
            scoreboard.over()

screen.exitonclick()
