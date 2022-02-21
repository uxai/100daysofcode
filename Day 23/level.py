from turtle import Turtle

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 1
        self.goto(-280, 250)
        self.set_level()

    def next_level(self):
        self.clear()
        self.score += 1
        self.set_level()

    def set_level(self):
        msg = "Level: " + str(self.score)
        self.write(msg, align="left", font=("Courier", 18))

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("Game Over", align="center", font=("Courier", 18, "bold"))