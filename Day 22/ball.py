from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.y_new = 3
        self.x_new = 3

    def move(self):
            new_y = self.ycor() + self.y_new
            new_x = self.xcor() + self.x_new
            self.goto(new_x, new_y)

    def wall_bounce(self):
        self.y_new *= -1

    def paddle_bounce(self):
        self.y_new *= - 1
        self.x_new *= -1

    def reset(self):
        self.speed(0)
        self.setpos(0, 0)
        self.paddle_bounce()
        self.speed('normal')
    