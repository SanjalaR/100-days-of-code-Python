
import turtle
from turtle import Turtle, Screen

screen = Screen()
import random

race = False
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-100, -50, 0, 50, 100, 150]
turtles = []

for i in range(0,6):
    tim = Turtle("turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230, y=y_pos[i])
    turtles.append(tim)

if bet:
    race = True

while race:

    for turtle in turtles:
        if turtle.xcor()>230:
            race = False
            winner = turtle.pencolor()
            if winner == bet:
                print(f"You win! Winner is {winner}")
            else:
                print(f"You lose! Winner is {winner}")
        turtle.forward(random.randint(0,10))


screen.exitonclick()
