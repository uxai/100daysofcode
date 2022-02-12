from turtle import Turtle

class Snake:

    def __init__(self):
        self.level = 1
        self.body = []
        self.create_snake()

    def create_snake(self):
        for s in range(0, 10):
            self.body.append(Turtle(shape="square"))
            self.body[s].penup()
            self.body[s].color("white")
            self.body[s].setpos(x=s*-20, y=0)

    def move(self):
        for seg_num in range(9, 0, -1):
            new_x = self.body[seg_num - 1].xcor()
            new_y = self.body[seg_num - 1].ycor()
            self.body[seg_num].goto(new_x, new_y)

        self.body[0].forward(self.level * 20)

    def up(self):
        if self.body[0].heading() != 270:
            self.body[0].seth(90)
    
    def down(self):
        if self.body[0].heading() != 90:
            self.body[0].seth(270)

    def left(self):
        if self.body[0].heading() != 0:
            self.body[0].seth(180)

    def right(self):
        if self.body[0].heading() != 180:
            self.body[0].seth(0)