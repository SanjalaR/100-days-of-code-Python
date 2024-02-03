import turtle

import pandas

screen = turtle.Screen()
screen.title("India States Game")

image = "new.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_coords(x, y):
#     print(x)
#     print(y)
#
#
# turtle.onscreenclick(get_mouse_coords)
# turtle.mainloop()

data = pandas.read_csv("states.csv")
data_list = data["State"].to_list()
score = 0
answers = []

for i in range(28):
    answer = screen.textinput(title=f"{score}/28 States Correct", prompt="Enter the name of a state: ").title()

    if answer == "Exit":
        break

    if answer in data_list:
        answers.append(answer)
        score += 1
        row = data[data.State == answer]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(row.x), int(row.y))
        t.write(row.State.item())

learn = []
for state in data_list:
    if state not in answers:
        learn.append(state)

new = pandas.DataFrame(learn)
new.to_csv("to_learn.csv")
print(new)

# screen.exitonclick()
