#Calculate leap year
def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False

def days_in_month(year = 2022, month=2):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        month_days[1] = 29
    return month_days[month-1]


year = int(input("Enter a year: "))
month = int(input("Enter a month (e.g. 12): "))

days = days_in_month(year, month)
print(days)

