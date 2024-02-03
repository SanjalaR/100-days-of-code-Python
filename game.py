import turtle

import pandas

screen = turtle.Screen()
screen.title("Name the States")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# To get x and y coords of all states
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")

data_list = data["state"].to_list()
print(data_list)
score = 0
answers = []

for i in range (50):
    answer = screen.textinput(f"{score}/50 States Correct", "Enter the name of a state: ").title()

    if answer == "Exit":
        break

    if answer in data_list:
        answers.append(answer)
        score += 1
        states = data[data.state == answer]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(states.x), int(states.y))
        t.write(states.state.item())

learn = [state for state in data_list if state not in answers]
# for state in data_list:
#     if state not in answers:
#         learn.append(state)
new = pandas.DataFrame(learn)
new.to_csv("to_learn.csv")
print(new)
