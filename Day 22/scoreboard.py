from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(x, y)
        self.set_score()

    def add_score(self):
        self.clear()
        self.score += 1
        self.set_score()

    def set_score(self):
        self.write(self.score, align="center", font=("Courier", 50))