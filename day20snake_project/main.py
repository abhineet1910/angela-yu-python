from turtle import  Screen
import time

import scoreboard
from food import Food
from snake import Snake
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("MY SNAKE GAME")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = scoreboard.Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_over = True
while game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # for t in segment:
    #     t.forward(20)
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_over = False
        scoreboard.game_over()
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 15:
            game_over = False
            scoreboard.game_over()
#collision detection



# t = Turtle()
# t.shape("square")
# t.color("white")
# t.fillcolor("white")
# v =  Turtle()
# v.shape("square")
# v.color("white")
# v.fillcolor("white")
# v.goto(x=-20,y=0)
# x = Turtle()
# x.shape("square")
# x.color("white")
# x.fillcolor("white")
# x.goto(x=-40,y=0)

























screen.exitonclick()