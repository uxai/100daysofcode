# Solving the maze puzzle for Reeborg's World
# https://reeborg.ca
# Code must be run in the reeborg env. to function properly

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def face_north():
    while is_facing_north() == False:
        turn_left()

face_north()

while not at_goal():
   while front_is_clear() and is_facing_north():
       move()
        
   if front_is_clear() and right_is_clear() == False:
       move()
   else:
       if right_is_clear():
           turn_right()
           if front_is_clear():
                move()
       else:
           turn_left()