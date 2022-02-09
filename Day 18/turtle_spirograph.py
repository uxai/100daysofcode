#Random walk

from turtle import Turtle, Screen
import random

def paint_color():
    R = random.randint(1, 255)
    G = random.randint(1, 255)
    B = random.randint(1, 255)
    tim.pencolor((R, G, B))

tim = Turtle()
tim.speed(0)
screen = Screen()
screen.colormode(255)

for _ in range(1, 37):
    paint_color()
    tim.circle(100)
    tim.left(10)

screen.exitonclick()