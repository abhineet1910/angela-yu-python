import turtle

import scoreboard
from paddle import Paddle
from turtle import Turtle, Screen
from ball import Ball
import time
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("#8B0000")
screen.title("PING BONG")
screen.tracer(0)
ball = Ball()
scoreboard = Scoreboard()


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")


while scoreboard:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # ball touches the walll upper and lower
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
#     detect collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor()>320:
        ball.bounce_x()

    #     alse bounce back the ball in opposite direction
    if ball.distance(l_paddle) < 50 and ball.xcor()<-320:
        ball.bounce_x()
    #     misses right side paddle
    if ball.xcor()>380:
        ball.reset()
        scoreboard.l_point()


    #     misses left side paddle
    if ball.xcor()<-380:
        ball.reset()
        scoreboard.r_point()
    scoreboard.game_over()
        # print("pond game over")
































screen.exitonclick()
