from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.score_bor()

    def score_bor(self):
        self.clear()
        self.goto(-150, 230)
        self.write(f"Score = {self.l_score}", align="center", font=("courier", 20, "normal"))
        self.goto(150, 230)
        self.write(f"Score = {self.r_score}", align="center", font=("courier", 20, "normal"))

    def l_point(self):
        self.l_score += 1
        self.score_bor()

    def r_point(self):
        self.r_score += 1
        self.score_bor()
