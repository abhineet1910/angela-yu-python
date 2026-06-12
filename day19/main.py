from turtle import Turtle,  Screen
tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
def turn_right():
    tim.right(10)

def clear():
    tim.clear()
    tim.home()

screen.listen()
screen.onkey(move_forward, "s")
screen.onkey(move_backward, "w")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")

screen.exitonclick()