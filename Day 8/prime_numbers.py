import math

def check_prime(check):
    if check % 2 == 0:
        return False
    
    root = math.floor(math.sqrt(check))
    for i in range(3, root + 1, 2):
        if check % i == 0:
            return False
            
    return True

n = int(input("Check for a primer number: "))

if check_prime(n):
    print("It's a prime number")
else:
    print("It's not a prime number")