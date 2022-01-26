import random

names = input("Please give me everybody's name, separated by a comma: ").split(", ")

selection = random.randint(0, len(names) - 1)

print(f"{names[selection]} will pay the bill.")