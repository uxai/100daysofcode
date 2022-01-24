# Calculate days, weeks and months left if we are to live to 90 years old
age = input("What is your current age?")

years = 90 - int(age)
days = years * 365
weeks = years * 52
months = years * 12 

print(f"You have {months} months, {weeks} weeks and {days} days remaining in your life.")