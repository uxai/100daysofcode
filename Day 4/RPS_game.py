# Rock, paper, scissors game
import random

rps = ["🪨", "📃", "✂️"]

choice = int(input("What do you choose? 0 for Rock, 1 for Paper or 2 for Scissors: "))

if choice < 0 or choice >= 3:
    print("Invalid choice!")
else:
    print(f"You chose {rps[choice]}")

    npc = random.randint(0,2)
    print(f"Computer chose {rps[npc]}")

    if choice > npc:
        if choice == 2 and npc == 0:
            print("You lose!")
        else:
            print("You win!")
    elif choice < npc:
        if npc == 2 and choice == 0:
            print("You win!")
        else:
            print("You lose!")
    else:
        print("It's a draw!")