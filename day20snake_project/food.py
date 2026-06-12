import random
from turtle import Turtle,Screen


class Food(Turtle):


    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(0.8,0.8)
        self.color("#00FF00")
        self.speed("fastest")
        randum_x = random.randint(-260,260)
        randum_y = random.randint(-260,260)
        self.goto(randum_x,randum_y)

    def refresh(self):
        randum_x = random.randint(-260,260)
        randum_y = random.randint(-260,260)
        self.goto(randum_x,randum_y)
