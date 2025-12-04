MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def has_raw_materials(ingredients):
    for material in ingredients:
        if ingredients[material] > resources[material]:
            print(f"Sorry there is not enough {material}.")
            return False
    return True

def get_payment():
    quarters = float(input("how many quarters?: ")) * 0.25
    dimes = float(input("how many dimes?: ")) * 0.10
    nickles = float(input("how many nickles?: ")) * 0.05
    pennies = float(input("how many pennies?: ")) * 0.01
    return quarters + dimes + nickles + pennies

def calculate_payment(cash_in_hand, drink_cost):
    if cash_in_hand < drink_cost:
        print(f"Sorry there is not enough money. Money refunded.")
        return 0
    else:
        to_return = cash_in_hand - drink_cost
        print(f"Here is ${to_return} in change.")
        return drink_cost

def make_coffee(ingredients, drink):
    for material in ingredients:
        resources[material] -= ingredients[material]
    print(f"Here is your {drink} ☕️. Enjoy!")

def machine():
    is_off = False
    profit = float(0)
    while not is_off:
        order = input("What would you like? (espresso/latte/cappuccino): ")
        if  order == "off":
            is_off = True
        elif order == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${profit}")
        else:
            drink = MENU[order]
            if has_raw_materials(drink["ingredients"]):
                cash_received = get_payment()
                payment_received = calculate_payment(cash_received, drink["cost"])
                if payment_received > 0:
                    profit += payment_received
                    make_coffee(drink["ingredients"], order)


machine()