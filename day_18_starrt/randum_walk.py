import turtle as t
import random
from turtle import Screen
def randumwalk():
    tim = t.Turtle()
    tim.shape("turtle")

    ########### Challenge 4 - Random Walk ########
    colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
    directions = [0, 90, 180, 270]
    tim.pensize(10)
    tim.speed("fastest")
    for _ in range(200):
        tim.color(random.choice(colours))
        tim.forward(30)
        tim.setheading(random.choice(directions))

