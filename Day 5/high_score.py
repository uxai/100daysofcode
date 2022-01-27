# Print the highest score in a class

student_scores = input("Input the scores of each student, separated by commas: ").split(", ")

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0

for score in student_scores:
    if(highest_score < score):
        highest_score = score

print(f"The highest score in the class is {highest_score}")