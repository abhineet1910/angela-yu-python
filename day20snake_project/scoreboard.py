from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,268)
        self.write(f"score: {self.score}", align="center", font=("Courier", 24, "normal"))
        self.hideturtle()
    def update_score(self):
        self.write(f"score: {self.score}", align="center", font=("Courier", 24, "normal"))

    def game_over(self):
       self.goto(0,0)
       self.write("Game Over", align="center", font=("Impact", 24, "normal"))



    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()