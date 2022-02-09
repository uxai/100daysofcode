from turtle import Turtle, Screen
import random


def paint_color():
    R = random.randint(1, 255)
    G = random.randint(1, 255)
    B = random.randint(1, 255)
    tim.pencolor((R, G, B))

tim = Turtle()
tim.shape("turtle")
tim.color("Green")

screen = Screen()
screen.colormode(255)

for side in range(3, 11):
    angle = 360 / side
    paint_color()
    for _ in range(1, side+1):
        tim.forward(100)
        tim.left(angle)


screen.exitonclick()