print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? "))
pax = int(input("How many people will be splitting the bill? "))

tip_amount = bill * (tip / 100)
total = round(bill + tip_amount, 2)
split = round(total / pax, 2)

total = "{:.2f}".format(total)
split = "{:.2f}".format(split)

print(f"Your total is ${total}, and the individual split costs is ${split}")