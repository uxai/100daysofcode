#Calculate leap year
year = int(input("What year would you like to check for leap year? "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year} is a leap year!")
else:
    print(f"{year} is not a leap year!")