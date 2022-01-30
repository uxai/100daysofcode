import math

def calculate_buckets(width, height, cover):
    return(math.ceil(width * height / cover))

wall_width = float(input("What is the width of the wall (meters)? "))
wall_height = float(input("What is the height of the wall (meters)? "))

coverage = 5

buckets = calculate_buckets(wall_width, wall_height, coverage)

print(f"You will need to buy {buckets} buckets of paint.")