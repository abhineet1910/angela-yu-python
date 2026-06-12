from turtle import Screen, Turtle




class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
        self.game_is_on = True

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
    def game_over(self):
        if self.l_score == 5:
            self.game_is_on = False
            self.write(f"{self.l_score} player one wins the match ", align="center", font=("Courier", 20, "normal"))
        elif self.r_score == 5:
            self.game_is_on = False
            self.write(f"{self.r_score} player two wins the match ", align="center", font=("Courier", 20, "normal"))
        elif self.l_score == self.r_score and self.r_score == 5 :
            self.write(f"{self.l_score} {self.r_score} match draw  ", align="center", font=("Courier", 20, "normal"))
            self.game_is_on = False