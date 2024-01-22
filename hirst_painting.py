import random
turtle.colormode(255)

# import colorgram
#
# rgb_color = []
#
# colors = colorgram.extract("51MOIhs2JoL._AC_UF1000,1000_QL80_.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     my_tuple = (r, g, b)
#     rgb_color.append(my_tuple)
# print(rgb_color)

colors = [(236, 35, 108), (145, 28, 66), (239, 75, 36), (7, 148, 95), (222, 170, 45), (183, 158, 47), (44, 191, 232), (28, 127, 194), (254, 223, 0), (125, 192, 78), (85, 27, 92), (244, 219, 53), (178, 40, 98), (40, 168, 117), (208, 131, 165), (205, 56, 35), (239, 162, 194), (147, 26, 24), (242, 168, 158), (162, 211, 178), (140, 211, 232), (7, 115, 55), (26, 186, 225), (84, 133, 177), (163, 193, 227), (112, 9, 8)]
timmy.setheading(225)
timmy.penup()
timmy.speed("fastest")
timmy.hideturtle()
timmy.forward(300)
timmy.setheading(0)

for i in range(10):
    for j in range (10):
        timmy.dot(20, random.choice(colors))
        #timmy.penup()
        timmy.forward(50)
    #timmy.penup()
    timmy.left(90)
    timmy.forward(50)
    timmy.left(90)
    timmy.forward(50*10)
    timmy.left(180)

screen = Screen()
screen.exitonclick()
