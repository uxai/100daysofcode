# Pizza ordering python
pizza_size = input("What size pizza do you want (S, M, L)? ")
cheese = input("Do you want extra cheese (Y, N)? ")
pepperoni = input("Do you want Pepperoni added (Y, N)? ")

total_cost = 0

print("\nYour final order is:")
if pizza_size == "l" or pizza_size == "L":
    total_cost += 25
    print("A large pizza - $25")
elif pizza_size == "m" or pizza_size == "M":
    total_cost += 20
    print("A medium pizza - $20")
else:
    total_cost += 15
    print("A small pizza - $15")

if cheese == "y" or cheese == "Y":
    total_cost += 1
    print("Extra Cheese - $1")

if pepperoni == "y" or pepperoni == "Y":
    if pizza_size == "s" or pizza_size == "S":
        total_cost += 2
        print("Pepperoni Toppings - $2")
    else:
        total_cost += 3
        print("Pepperoni Toppings - $3")

print("------------------------------")
print(f"Total amount due is: ${total_cost:.2f}")


