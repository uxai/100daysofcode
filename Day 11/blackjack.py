import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
house = []
user = []

print('''
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                       _/ |                
                      |__/                 
''')

input("Press any key to begin game")

def deal_cards(hand):
    hand.clear()
    for _ in range(0, 2):
        select = random.randint(0, 12)
        hand.append(cards[select])

def add_card(hand):
    select = random.randint(0, 12)
    hand.append(cards[select])
    if sum(hand) > 21 and 11 in hand:
        index = hand.index(11)
        hand[index] = 1

def users_move():
    if sum(user) > 21:
        return
    else:
        print("+-------------------------+")
        print(f"Your hand is {user} with a total sum of {sum(user)}")
        print(f"House's revealed hand is {house[0]}")
        print("+-------------------------+")
        action = input("Would you like to hit(h) or stand(s)? ").lower()
        if action == "hit" or action == "h":
            add_card(user)
            users_move()



def play_blackjack():
    
    # Deal the cards for first hand
    deal_cards(house)
    deal_cards(user)

    users_move()
    user_total = sum(user)
    house_total = sum(house)

    while house_total < 16:
        add_card(house)
        house_total = sum(house)


    print("*-------------------------*")
    print(f"House has a hand of {house} and total of {house_total}!")
    print(f"You have a hand of {user} and total of {user_total}!")

    if user_total > 21:
        print("You exceeded 21, Bust!")
    elif house_total > 21:
        print(f"House Busts with a sum of {house_total}, You win!")
    elif user_total > house_total:        
        print("You win!")
    else:
        print("You Lose!")
        
    print("*-------------------------*")
    if input("Play Again? (y/n): ").lower() == "y":
        play_blackjack()

play_blackjack()