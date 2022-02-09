#Extract colors from zelda.jpg and make a hirst dot painting

from turtle import Turtle, Screen
import random
import colorgram

rgb_colors = []
colors = colorgram.extract('zelda.jpg', 100)

for color in colors:
    R = color.rgb.r
    G = color.rgb.g
    B = color.rgb.b
    rgb_colors.append((R,G,B))

tim = Turtle()
tim.speed(0)
tim.penup()

screen = Screen()
screen.colormode(255)
tim.pencolor((255, 255, 255))
tim.setpos(-350,-300)

for row in range(1, 11):
    for step in range(1, 11):
        tim.fillcolor(random.choice(rgb_colors))
        tim.pendown()
        tim.begin_fill()
        tim.circle(20)
        tim.end_fill()
        tim.penup()
        tim.forward(70)
    tim.backward(700)
    tim.left(90)
    tim.forward(70)
    tim.right(90)


screen.exitonclick()