from projects_data import python_course

leave = False

print('''
 _______  __   __  ___      ___      _______  _______  __   __  _______ 
|       ||  | |  ||   |    |   |    |   _   ||  _    ||  | |  ||       |
|  _____||  |_|  ||   |    |   |    |  |_|  || |_|   ||  | |  ||  _____|
| |_____ |       ||   |    |   |    |       ||       ||  |_|  || |_____ 
|_____  ||_     _||   |___ |   |___ |       ||  _   | |       ||_____  |
 _____| |  |   |  |       ||       ||   _   || |_|   ||       | _____| |
|_______|  |___|  |_______||_______||__| |__||_______||_______||_______|
''')

print("Course syllabus details from Angela Yu's course for #100DaysOfPython")
print("https://www.udemy.com/course/100-days-of-code/\n")

def check_progress():
    current_day = int(input("What day have you finished in the course? "))
    next_course = python_course[current_day]["Description"]

    print("\n==================")
    print(f"Congratulations! You are {current_day}% complete with the entire course!")
    print(f"The next course will cover {next_course}")
    print("==================\n")

def check_details():
    day = int(input("What lesson day would you like the details for? "))
    level = python_course[day - 1]["Level"]
    description = python_course[day - 1]["Description"]
    print("\n==================")
    print(f"The lesson level is {level}")
    print(f"The course covers {description}")
    print("==================\n")

while leave == False:
    choice = 0
    print("What would you like to do?")
    print("1. Check progress")
    print("2. Check class details by day")
    print("3. Exit program")
    while choice == 0:
        choice = int(input("Enter your choice (1, 2, 3): "))
        if choice != 1 and choice != 2 and choice != 3:
            print("Please enter a valid option")
            choice = 0

    if choice == 1:
        check_progress()
    elif choice == 2:
        check_details()
    else:
        leave = True

print("Thanks for using, Goodbye!")