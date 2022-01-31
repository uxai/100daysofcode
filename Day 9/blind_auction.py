import os

# define our clear screen function (For windows)
def clear():
    _ = os.system('cls')

# =============================
# START PROGRAM FOR AUCTION
# =============================
print('''
  ____  _ _            _        _              _   _             
 / ___|(_) | ___ _ __ | |_     / \  _   _  ___| |_(_) ___  _ __  
 \___ \| | |/ _ \ '_ \| __|   / _ \| | | |/ __| __| |/ _ \| '_ \ 
  ___) | | |  __/ | | | |_   / ___ \ |_| | (__| |_| | (_) | | | |
 |____/|_|_|\___|_| |_|\__| /_/   \_\__,_|\___|\__|_|\___/|_| |_|
                                                                 
''')
print("Welcome to the secret auction")

auctions = {}
continue_bidding = True

#Keep track of the highest bidder and their bid
highest_bidder = ""
highest_bid = 0

while continue_bidding:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))

    auctions[name] = bid
    clear()
    print(f"Thank you {name}! Your bid has been successfully submitted")

    more_bids = ""
    while more_bids != "no" and more_bids != "yes":
        more_bids = input("Are there any other bidders (yes/no)? ").lower()
        if more_bids != "no" and more_bids != "yes":
            print("Please enter a valid response.")

    if more_bids == "no":
        continue_bidding = False
    clear()

for bidder in auctions:
    if auctions[bidder] > highest_bid:
        highest_bid = auctions[bidder]
        highest_bidder = bidder

print("============")
print(f"The winner is {highest_bidder} with the bid of ${highest_bid}")
print("============")