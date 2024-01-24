from turtle import Turtle, Screen
from player import Player
from cars import Car
from scoreboard import ScoreBoard
import random
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("white")
screen.tracer(0)

player = Player()
car = Car()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(fun=player.up, key="Up")
screen.onkey(fun=player.down, key="Down")

game = True
while game:
    time.sleep(0.1)
    screen.update()
    car.create()
    car.start()
    for i in car.list:
        if player.distance(i) < 15:
            game = False
            scoreboard.lost()
            print("You lost!")
    if player.ycor() > 280:
        print("Level up!")
        player.goto(0, -280)
        car.increase()
        scoreboard.levelup()

screen.exitonclick()
