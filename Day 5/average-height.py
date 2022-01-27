total_students = 0
total_height = 0

student_heights = input("Input a list of student heights, separated by commas: ").split(", ")

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

for height in student_heights:
    total_students += 1
    total_height += height

average_height = round(total_height / total_students)
print(f"There are a total of {total_students} students with an average height of {average_height}")