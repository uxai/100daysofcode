# Password Generator

import random

password = ""

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['@', '!', '#', '$', '%', '&', '(', ')', '*', '+']

char_select = [letters, numbers, symbols]

print("Welcome to the PyPassword Generator")
num_letters = int(input("How many letters would you like in your password? "))
num_numbers = int(input("How many numbers would you like? "))
num_symbols = int(input("How many symbols would you like? "))

total_char = num_letters + num_symbols + num_numbers

# Checks to see if any character set was not requested by user
if num_letters == 0:
    char_select.remove(letters)

if num_numbers == 0:
    char_select.remove(numbers)

if num_symbols == 0:
    char_select.remove(symbols)

for character in range(1, total_char + 1):

    # select a random between letters, numbers and symbols for next character in the password
    # req checks the current length of char_select for updated requirements
    req = len(char_select) - 1
    rand = random.randint(0, req)

    # Gets the length of the sub-list that was randomly selected
    char_range = len(char_select[rand]) - 1
 
    if char_select[rand] == letters and num_letters != 0:
        rand_letter = random.randint(0, char_range) 
        password += char_select[rand][rand_letter]
        #reduce the number of letters required by one
        # Removes letters from our list of options when exhausted
        num_letters -= 1
        if(num_letters == 0):
            char_select.remove(letters)

    elif char_select[rand] == numbers and num_numbers != 0:
        rand_number = random.randint(0, char_range) 
        password += char_select[rand][rand_number]
        #reduce the number of numbers required by one
        # Removes numbers from our list of options when exhausted
        num_numbers -= 1
        if(num_numbers == 0):
            char_select.remove(numbers)

    elif char_select[rand] == symbols and num_symbols != 0:
        rand_symbol = random.randint(0, char_range)
        password += char_select[rand][rand_symbol]
        #reduce the number of symbols required by one
        # Removes symbols from our list of options when exhausted
        num_symbols -= 1
        if(num_symbols == 0):
            char_select.remove(symbols)

print(f"Your new password is: {password}")