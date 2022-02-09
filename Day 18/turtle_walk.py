#Random walk

from turtle import Turtle, Screen
import random

def paint_color():
    R = random.randint(1, 255)
    G = random.randint(1, 255)
    B = random.randint(1, 255)
    tim.pencolor((R, G, B))

def change_direction():
    direction = [0, 90, 180, 270]
    return random.choice(direction)

tim = Turtle()
tim.shape("turtle")
tim.color("Green")
tim.pensize(10)
tim.speed(5)

screen = Screen()
screen.colormode(255)

while True:
    paint_color()
    tim.left(change_direction())
    tim.forward(50)

screen.exitonclick()