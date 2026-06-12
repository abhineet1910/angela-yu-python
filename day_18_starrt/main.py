from random import choice, random
import turtle
from turtle import*
#this will import all the thing in the module

from turtle import Turtle
#this will import the specif class from the module from module import class
tim= turtle.Turtle()
tim.shape("turtle")
tim.speed("fastest")
for i in range(3):
    tim.color("red")
    tim.forward(50)
    tim.right(120)
for i in range(4):
    tim.color("blue")
    tim.forward(50)
    tim.right(90)
for i in range(5):
    tim.color("green")
    tim.forward(50)
    tim.right(72)
for i in range(6):
    tim.color("yellow")
    tim.forward(50)
    tim.right(60)
for i in range(7):
    tim.color("#FF69B4")
    tim.forward(50)
    tim.right(51.4)
for i in range(8):
    tim.color("#FF00FF")
    tim.forward(50)
    tim.right(45)
for i in range(9):
    tim.color("#00FF00")
    tim.forward(50)
    tim.right(40)
for i in range(10):
    tim.color("#FFA500")
    tim.forward(50)
    tim.right(36)
def draw_shape(num_side):
    angle = 360 / num_side
    for i in range(num_side):
        tim.forward(100)
        tim.left(angle)
colors = ["#F0F8FF","#B0C4DE","#6495ED","#4169E1","#0000FF","#0000CD","#000080"]
for i in range(3,11):
    tim_colour = choice(colors)
    tim.color(tim_colour)
    draw_shape(i)
# tinny=Turtle()
# tinny.shape("turtle")
# tinny.color("red")
# # tinny.right(180)
# for i in range (20):
#     tim.forward(10)
#     tinny.forward(10)
#     tinny.penup()
#     tim.penup()
#     tim.forward(10)
#     tinny.forward(10)
#     tinny.pendown()
#     tim.pendown()
# # for i in range(4):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#
#
#     tinny.forward(20)
#     tinny.penup()
#     tinny.forward(20)
#     tinny.pendown()
#     tim.left(90)
#     tinny.right(90)
# tim.left(180)
# tinny.right(180)
# for i in range(4):
#
#     tinny.forward(20)
#     tinny.penup()
#     tinny.forward(20)
#     tinny.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#     tim.right(90)
#     tinny.left(90)

# tinny_turtle.pencolor("#00FF00")
# tinny_turtle.fillcolor("#191970")
tim.color("#00FF00", "#191970")
# for i in range(4):
#     tim.forward(100)
#     tim.left(90)
# # tinny_turtle.forward(100)
# tinny_turtle.left(90)
# tinny_turtle.forward(100)
# tinny_turtle.left(90)
# tinny_turtle.forward(100)

tim.resizemode("auto")
import heros



import randum_walk
tinny = randum_walk.randumwalk()
import make_a_spirograph
thus = make_a_spirograph.random_color()
tim.speed("fastest")
tim.shape("turtle")
tim.pensize(5)
thus = make_a_spirograph.draw_spirograph(5)




















screen= turtle.Screen()
screen.exitonclick()
