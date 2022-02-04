# The higher lower game
import os
import random
from game_data import data

def clear():
    _ = os.system('cls')

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """*-----------*
|  VERSUS   |
*-----------*"""

def get_user(first):
    id = random.randint(0, len(data) - 1)
    if id == first:
        get_user
    else:
        return id

def check_answer(response, first, second):
    if first > second and response == "A":
        return True
    elif second > first and response == "B":
        return True
    else:
        return False


def play():
    # Keep track of the current score, and if they get the answer correct
    score = 0
    scored = True

    while scored == True:
        clear() # Clear the screen
        print(logo)
        # assign the id that will be used in the first comparison
        if score == 0:
            # If its the first time around, apply a random index to the first
            first = random.randint(0, len(data) - 1)
        else:
            print(f"That's right! You ave a score of {score}\n")
            first = second # Move second to the first position
        second = get_user(first)

        print(f"Compare A: {data[first]['name']}, {data[first]['description']} from {data[first]['country']} ")
        print(vs)
        print(f"Compare B: {data[second]['name']}, {data[second]['description']} from {data[second]['country']} ")
        response = input("Who has more followers? Type 'A' or 'B': ")

        # Check if the user scored
        scored = check_answer(response, data[first]['follower_count'],  data[second]['follower_count'])
        if scored == True:
            score += 1
        else:
            print("------------")
            print(f"Sorry, wrong answer, your final score is: {score}")
    

play()