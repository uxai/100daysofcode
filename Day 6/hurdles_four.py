# Assignment answer for Reeborg's World Hurdle 4.
# https://reeborg.ca
# Code must be run in the reeborg env. to function properly

def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def hurdle():
    turn_left()
    while not right_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    
    
while not at_goal():
    if front_is_clear():
        move()
    else:
        hurdle()