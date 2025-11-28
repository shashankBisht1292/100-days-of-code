from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

all_operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculate():
    should_continue = True
    first_num = float(input("What's the first number?: "))

    while should_continue:
        for ops in all_operations:
            print(ops)
        operator = input("Pick an operation: ")
        second_num = float(input("What's the next number?: "))

        answer = all_operations[operator](first_num, second_num)
        print(f"{first_num} {operator} {second_num} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            first_num = answer
        else:
            should_continue = False
            print("\n" * 50)
            calculate()


calculate()

