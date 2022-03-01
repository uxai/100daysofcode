with open("file1.txt") as one:
    one_file = [line.strip() for line in one]
with open("file2.txt") as two:
    two_file = [line.strip() for line in two]

final = [int(num) for num in two_file if num in one_file]

print(final)