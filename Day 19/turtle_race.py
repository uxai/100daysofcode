from turtle import Turtle, Screen
import random

screen = Screen()

race_on = False

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet", prompt="Which color turtle do you want to bet on?")
print(f"You bet on the {user_bet} turtle")

colors = ("red", "orange", "yellow", "green", "blue", "purple")

turtles = []

for maker in range(0, 6):
    y_coord = -125 + maker * 50
    turtles.append(Turtle(shape="turtle"))
    turtles[maker].color(colors[maker])
    turtles[maker].penup()
    turtles[maker].goto(x=-230, y=y_coord)

if user_bet.lower() in colors:
    race_on = True

while race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")
            race_on = False
        steps = random.randint(0,10)
        turtle.forward(steps)


screen.exitonclick()