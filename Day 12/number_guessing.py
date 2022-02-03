# Number guessing game.
import random

MYSTERY_NUMBER = random.randint(1, 100)

print('''


    ______     __  __     ______     ______     ______        ______   __  __     ______        __   __     __  __     __    __     ______     ______     ______    
   /\  ___\   /\ \/\ \   /\  ___\   /\  ___\   /\  ___\      /\__  _\ /\ \_\ \   /\  ___\      /\ "-.\ \   /\ \/\ \   /\ "-./  \   /\  == \   /\  ___\   /\  == \   
   \ \ \__ \  \ \ \_\ \  \ \  __\   \ \___  \  \ \___  \     \/_/\ \/ \ \  __ \  \ \  __\      \ \ \-.  \  \ \ \_\ \  \ \ \-./\ \  \ \  __<   \ \  __\   \ \  __<   
    \ \_____\  \ \_____\  \ \_____\  \/\_____\  \/\_____\       \ \_\  \ \_\ \_\  \ \_____\     \ \_\\"\_\  \ \_____\  \ \_\ \ \_\  \ \_____\  \ \_____\  \ \_\ \_\ 
     \/_____/   \/_____/   \/_____/   \/_____/   \/_____/        \/_/   \/_/\/_/   \/_____/      \/_/ \/_/   \/_____/   \/_/  \/_/   \/_____/   \/_____/   \/_/ /_/ 
                                                                                                                                                                    


''')
print("Welcome to the number guessing game!")

def play_game():
    guess = int(input("Guess a number from 1 and 100: "))
    if guess == MYSTERY_NUMBER:
        print(f"You win! The number was {MYSTERY_NUMBER}")
        return True
    elif guess > MYSTERY_NUMBER:
        print("You guessed too high!")
        return False
    else:
        print("You guessed too low!")
        return False

def initiate_game():
    # Select difficulty
    player_lives = 10
    player_win = False
    difficulty = input("Select your difficulty - Easy or Hard? ").lower()
    if difficulty != "easy" and difficulty != "hard":
        initiate_game()
    else:
        if difficulty == "easy":
            player_lives = 10
        else:
            player_lives = 5

    while player_win == False and player_lives > 0:
        print(f"You have {player_lives} lives remaining.")
        player_win = play_game()
        player_lives -= 1

    if player_win == False:
        print(f"You are out of guesses! The number was {MYSTERY_NUMBER}")

initiate_game()