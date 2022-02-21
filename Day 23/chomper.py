from turtle import Turtle

class Chomper(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.speed(0)
        self.setheading(90)
        self.goto_start()

    def move(self):
        self.forward(20)
    
    def goto_start(self):
        self.setposition(0, -270)
