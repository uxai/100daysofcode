def add(*args):
    sum = 0
    for arg in args:
        sum += int(arg)
    print(sum)

add(5, 10, 15, 20, 25, 30, 35)

def calculate(**kwargs):
    for key, value in kwargs.items():
        print(key)

calculate(add=3, multiply=5)