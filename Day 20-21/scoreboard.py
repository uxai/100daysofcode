from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.shape("blank")
        self.penup()
        self.setpos(0, 260)
        self.set_score()
        

    def set_score(self):
        self.write(f"Score: {self.score}", align="center", font=('courier', 18))

    def add_score(self):
        self.clear()
        self.score += 1
        self.set_score()

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", align='center', font=('courier', 18, 'bold'))