import random
import turtle
from turtle import Turtle, Screen
# user_bet = input("bet on the colour you thing gonna wins ...")
# tim = Turtle()
screen = Screen()
# tim.shape("turtle")
# tim.color("purple")
# tommy = Turtle()
# tommy.shape("turtle")
# tommy.color("red")
# tuffy = Turtle()
# tuffy.shape("turtle")
# tuffy.color("blue")
# tiger = Turtle()
# tiger.shape("turtle")
# tiger.color("green")
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",prompt="which turtle will win the race? ENTER THE COLOUR !")


sped = [0,1,2,3,4,5,6,7,8,9,10]
red = random.choice(sped)
y_positions = [-100, -50, 0, 50]

turtles = []

colors = ["purple", "red", "blue", "green", "yellow", "orange"]

y_positions = []

start_y = -150   # safe margin from bottom
gap = 60         # distance between turtles

for i in range(len(colors)):
    y_positions.append(start_y + i * gap)

for i in range(len(colors)):
    t = Turtle()
    t.shape("turtle")
    t.color(colors[i])
    t.penup()
    t.goto(x=-230, y=y_positions[i])  # starting line
    turtles.append(t)
is_race_on = True
y_positions = []

while is_race_on:
    for t in turtles:
        distance = random.randint(0, 10)
        t.forward(distance)
        t.speed(red)

        if t.xcor() > 230:  # finish line
            is_race_on = False
            winning_color = t.pencolor()

if user_bet == winning_color:
    print("You win!")
else:
    print(f"You lose! The winner is {winning_color}")