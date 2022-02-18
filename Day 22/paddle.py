from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.speed(0)
        self.setpos(x, y)

    def up(self):
        if self.ycor() < 240:
            new_pos = self.ycor() + 20
            self.goto(self.xcor(), new_pos)

    def down(self):
        if self.ycor() > -240:
            new_pos = self.ycor() - 20
            self.goto(self.xcor(), new_pos)