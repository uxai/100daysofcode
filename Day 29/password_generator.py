# Password Generator
import random

def password_generator():

    LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    SYMBOLS = ['@', '!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters = [random.choice(LETTERS) for _ in range(1, random.randint(8, 12))]
    numbers = [random.choice(NUMBERS) for _ in range(1, random.randint(4, 6))]
    symbols = [random.choice(SYMBOLS) for _ in range(1, random.randint(4, 6))]

    password = letters + numbers + symbols
    random.shuffle(password)

    new_password = "".join(password)

    return new_password