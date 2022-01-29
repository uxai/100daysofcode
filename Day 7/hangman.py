import random

gameover = False
lives = 6
word_list = ["ardvark", "baboon", "camel", "balloon", "rabbit", "astronaut", "flowery", "malicious", "actually", "guarded", "quiver", "children", "judicious", "zoom", "collect", "goofy", "expensive", "floor", "fanatical", "gaze", "damage", "wood", "coil", "obsolete", "payment", "woebegone", "opposite", "unwritten", "tour", "interest", "poke", "abstracted", "choke", "sticks", "hope", "replace", "property", "unfasten", "rainy", "scarf", "forgetful", "greasy", "swift", "vigorous", "load", "beds", "hypnotic", "summer", "woman", "laughable", "glossy", "wooden", "knock", "reflect", "lonely", "hour"]
hearts = ["♥", "♥♥", "♥♥♥", "♥♥♥♥", "♥♥♥♥♥", "♥♥♥♥♥♥"]

# Get a random index for the word_list and assign the chosen word
word_count = len(word_list)
selection = random.randint(0, word_count - 1)
chosen_word = word_list[selection]

blank_word = []

for _ in chosen_word:
    blank_word += "_"

def print_progress():
    merge = ""
    for char in blank_word:
        merge += f"{char} "
    print(merge)

print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
''')

while gameover == False:
    print_progress()
    print(f"Lives remaining: {hearts[lives-1]}")
    guess = input("Guess a letter: ").lower()

    if guess in chosen_word:
        print("Good job!\n")
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                blank_word[position] = guess
    else:
        print(f"{guess} is not in the word\n")
        lives -= 1

    if '_' not in blank_word:
        print(f"Congratulations! You guessed on the letters in {chosen_word}!")
        gameover = True
    
    if lives == 0:
        print("Gameover, you're out of lives!")
        print(f"The word was: {chosen_word}")
        gameover = True