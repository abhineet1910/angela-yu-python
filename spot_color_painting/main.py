import random

import colorgram
import turtle as turtle_module
from turtle import Screen

# rgb_colours = []
#
# # extract 10 colors (you can change this number)
# colours = colorgram.extract('paint.jpg', 10)
#
# for color in colours:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colours.append((r, g, b))
#
# print(rgb_colours)
turtle_module.colormode(255)
colour = [(233, 233, 232), (231, 233, 237), (236, 231, 234), (222, 232, 226), (208, 160, 82), (54, 89, 131), (146, 91, 40), (140, 26, 48), (222, 206, 108), (132, 177, 203)]
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
for i in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(colour))
    tim.forward(50)
    if i % 10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)










































screen = Screen()
screen.exitonclick()
