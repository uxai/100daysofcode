row1 = ["⬛", "⬛", "⬛"]
row2 = ["⬛", "⬛", "⬛"]
row3 = ["⬛", "⬛", "⬛"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

location = input("Where would you like to put the treasure? ")

map[int(location[1]) - 1][int(location[0]) - 1] = "X"
print(f"{row1}\n{row2}\n{row3}")
