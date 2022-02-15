from turtle import Turtle

class Snake:

    def __init__(self):
        self.body = []
        self.create_snake()

    def create_snake(self):
        for s in range(0, 3):
            self.build_snake(s)

    def build_snake(self, position):
            self.body.append(Turtle(shape="square"))
            self.body[position].penup()
            self.body[position].color("white")
            self.body[position].setpos(x=position*-20, y=0)

    def grow(self):
        self.body.append(Turtle(shape="square"))
        self.body[-1].penup()
        self.body[-1].color("white")
        self.body[-1].setpos(self.body[-2].xcor(), self.body[-2].ycor())

    def move(self):
        for seg_num in range(len(self.body) - 1, 0, -1):
            new_x = self.body[seg_num - 1].xcor()
            new_y = self.body[seg_num - 1].ycor()
            self.body[seg_num].goto(new_x, new_y)

        self.body[0].forward(20)

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