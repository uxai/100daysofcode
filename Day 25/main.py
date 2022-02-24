import turtle
import csv

STATESCSV = "50_states.csv"

screen = turtle.Screen()
map = "blank_states_img.gif"
screen.addshape(map)
screen.setup(width=725, height=491)

board = turtle.Turtle()
board.shape(map)

labels = turtle.Turtle()
labels.penup()
labels.hideturtle()

states_found = []

while len(states_found) < 50:
    state = screen.textinput(f"States: {len(states_found)}/50", "Enter a state name")
    with open(STATESCSV) as file:
        for line in file:
            if state in line and state not in states_found:
                stored_line = line.split('\n')
                detail = stored_line[0].split(',')
                states_found.append(detail[0])
                labels.setpos(int(detail[1]), int(detail[2]))
                labels.write(detail[0], align="center", font=("Courier", 12))
                break

screen.exitonclick()