with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("my_filetwo.txt", "w") as file:
    file.write("Hola!")