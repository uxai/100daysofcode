# Solving the maze puzzle for Reeborg's World
# https://reeborg.ca
# Code must be run in the reeborg env. to function properly

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
        if right_is_clear():
            if is_facing_north() == False or front_is_clear() == False:
                turn_right()
    else:
        turn_left()