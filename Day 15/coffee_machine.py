# Creating a coffee machine
import os
def clear():
    _ = os.system('cls') # Clear screen for windows

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
machine = {
    "resources": {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    },
    "money": 0,
}

def check_resources(drink):
    if MENU[drink]["ingredients"]["water"] <= machine["resources"]["water"] and MENU[drink]["ingredients"]["milk"] <= machine["resources"]["milk"] and MENU[drink]["ingredients"]["coffee"] <= machine["resources"]["coffee"]:
        return True
    else:
        return False

def print_report():
    print("------------------------\nCOFFEE MACHINE REPORT:")
    print(f"Water: {machine['resources']['water']}ml")
    print(f"Milk: {machine['resources']['milk']}ml")
    print(f"Coffee: {machine['resources']['coffee']}ml")
    print(f"Revenue: ${float(machine['money']):.2f}")

def refill_machine():
    global machine
    machine["resources"]["water"] = 300
    machine["resources"]["milk"] = 200
    machine["resources"]["coffee"] = 100
    print("Refill of resources successfully completed!")

def brew_coffee(drink):
    machine["resources"]["water"] -= MENU[drink]["ingredients"]["water"]
    machine["resources"]["milk"] -= MENU[drink]["ingredients"]["milk"]
    machine["resources"]["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    print("☕ Enjoy your coffee!")

def request_money(cost):
    print(f"Please pay an amount of ${cost:.2f}")
    quarters = int(input("How many quarters are you inserting? "))
    dimes = int(input("How many dimes are you inserting? "))
    knickles = int(input("How many knickles are you inserting? "))
    pennies = int(input("How many pennies are you inserting? "))
    money_inserted = quarters * .25 + dimes *.1 + knickles *.05 + pennies * .01
    print("------------------------")
    if money_inserted >= float(cost):
        machine["money"] += cost
        refund = money_inserted - cost
        if refund > 0:
            print(f"Payment of ${money_inserted:.2f} received successfully, you will be refunded ${refund:.2f}")
            return True
        else:
            print(f"Payment of ${money_inserted:.2f} received successfully")
            return True
        
    else:
        print("Insufficient funds, please try again.")
        return False

def boot_machine():
    print("""
                       .
                        `:.
                          `:.
                  .:'     ,::
                 .:'      ;:'
                 ::      ;:'
                  :    .:'
                   `.  :.
          _________________________
         : _ _ _ _ _ _ _ _ _ _ _ _ :
     ,---:".".".".".".".".".".".".":
    : ,'"`::.:.:.:.:.:.:.:.:.:.:.::'
    `.`.  `:-===-===-===-===-===-:'
      `.`-._:                   :
        `-.__`.               ,' met.
    ,--------`"`-------------'--------.
     `"--.__                   __.--"'
            `""-------------""'
    """)
    print("1. Espresso")
    print("2. Latte")
    print("3. Cappuccino")
    print("4. Refill")
    print("5. Report")
    print("6. Turn Off Machine")
    print("------------------------")
    while True:
        selection = int(input("Welcome to CoinCoffee, please type a selection from the menu above: "))
        if selection >= 1 and selection <= 6:
            break

    if selection >=1 and selection <= 3:
        if selection == 1:
            drink = "espresso"
        elif selection == 2:
            drink = "latte"
        else:
            drink = "cappuccino"

        if check_resources(drink):
            if request_money(MENU[drink]["cost"]):
                brew_coffee(drink)
        else:
            print("Not enough resources to complete your request.")
    elif selection == 4:
        refill_machine()
    elif selection == 5:
        print_report()
    else:
        print("Shutting down...")
        return
    
    input("Press any key to continue.")
    # Recursive until machine is shutdown.
    clear()
    boot_machine()


boot_machine()