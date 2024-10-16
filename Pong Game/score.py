from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()
        self.score_1 = 0
        self.score_2 = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.score_2, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.score_1, align="center", font=("Courier", 80, "normal"))

    def score_2_point(self):
        self.score_2 += 1
        self.update_score()

    def score_1_point(self):
        self.score_1 += 1
        self.update_score()