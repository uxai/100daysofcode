# Turtle Python project
# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DarkOliveGreen4")
# timmy.forward(100)

# my_screen = Screen()
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon Name", ["Squirtle", "Bulbasaur", "Charmander", "Pikachu"])
table.add_column("Type", ["Water", "Grass", "Fire", "Electric"])
table.align = 'l'
print(table)