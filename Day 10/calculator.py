def add (n1, n2):
    return n1 + n2

def subtract (n1, n2):
    return n1 - n2

def divide (n1, n2):
    if n2 == 0:
        print("Cannot divide by 0")
        return
    else:
        return n1 / n2

def multiply (n1, n2):
    return n1 * n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculation():
    num1 = float(input("What is the first number? "))

    response = "y"
    while response == "y":
        num2 = float(input("What is the next number? "))

        for operator in operations:
            print(operator)
        select_operator = input("Please select a operator listed: ")

        # Calls the function associated to the given key
        arithmetic = operations[select_operator]
        answer = arithmetic(num1, num2)
        if answer != None:
            print(f"{num1} {select_operator} {num2} = {answer}")
        else:
            print("Please try a new calculation.")
            calculation()

        response = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
        if response == "y":
            num1 = answer
        else:
            calculation()

calculation()