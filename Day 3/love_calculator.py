# A love calculator
print("Welcome to the love calculator!")
your_name = input("What is your name? ").lower()
their_name = input("What is their name? ").lower()

count_true = your_name.count("t") + your_name.count("r") + your_name.count("u") + your_name.count("e") + their_name.count("t") + their_name.count("r") + their_name.count("u") + their_name.count("e")

count_love = your_name.count("l") + your_name.count("o") + your_name.count("v") + your_name.count("e") + their_name.count("l") + their_name.count("o") + their_name.count("v") + their_name.count("e")

love_score = int(str(count_true) + str(count_love))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos")
elif love_score > 40 and love_score < 50:
    print(f"Your score is {love_score}, you are alright together")
else:
    print(f"Your love score is {love_score}")