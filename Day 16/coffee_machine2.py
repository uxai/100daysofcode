from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

vendor = MoneyMachine()
brewer = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "report":
        vendor.report()
        brewer.report()
    elif choice == "off":
        is_on = False
    else:
        drink = menu.find_drink(choice)
        if brewer.is_resource_sufficient(drink) and vendor.make_payment(drink.cost):
            brewer.make_coffee(drink)
