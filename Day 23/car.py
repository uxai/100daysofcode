import random
from turtle import Turtle

class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.speed(0)
        self.turtlesize(stretch_len=2, stretch_wid=1)
        self.setheading(180)
        self.penup()
        self.starting()
        
    def starting(self):
        starty = random.randint(-220, 220)
        self.setposition(300, starty)

    def move(self):
        self.forward(10)