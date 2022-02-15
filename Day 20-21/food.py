from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("yellow")
        self.speed("fastest")
        randx = random.randint(-280, 280) + 5
        randy = random.randint(-280, 280) + 5
        self.goto(randx, randy)
        self.refresh()

    def refresh(self):
        randx = random.randint(-280, 280) + 5
        randy = random.randint(-280, 280) + 5
        self.goto(randx, randy)