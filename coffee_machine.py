"""
Types of coffee: Espresso -1.50 (50ml water, 18g coffee),
                Latte -2.50 (200ml water, 24g coffee, 150ml milk),
                Cappuccino -3.00 (250ml water, 24g coffee, 100ml milk)
Start: 300ml water, 200ml milk, 100g coffee
Currency: Penny(0.01), Dime(0.10), Nickel(0.05), Quarter(0.25)
"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
    "money": 0,
}


def check_res(entry):
    if MENU[entry]["ingredients"]["water"] > resources["water"]:
        print("Sorry there is not enough water.")
        return False
    if MENU[entry]["ingredients"]["milk"] > resources["milk"]:
        print("Sorry there is not enough milk.")
        return False
    if MENU[entry]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry there is not enough coffe.")
        return False
    return True


def make_coffee(entry):
    resources["water"] -= MENU[entry]["ingredients"]["water"]
    resources["milk"] -= MENU[entry]["ingredients"]["milk"]
    resources["coffee"] -= MENU[entry]["ingredients"]["coffee"]


def coffee_machine():
    entry = input("What would you like? (espresso/latte/cappuccino/report): ")
    if entry == "report":
        print(
            f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']}\n")
        coffee_machine()
    elif entry == "off":
        return
    else:
        if check_res(entry):
            cost = MENU[entry]["cost"]
            print("Please insert coins.")
            q = int(input("How many quarters?: ")) * 0.25
            d = int(input("How many dimes?: ")) * 0.10
            n = int(input("How many nickels?: ")) * 0.05
            p = int(input("How many pennies?: ")) * 0.01
            paid = q + d + n + p
            if paid < cost:
                print("Sorry that's not enough money. Money refunded.")
            else:
                change = paid - cost
                print(f"Here is ${change} in change.")
                resources["money"] += cost
                make_coffee(entry)
                print(f"Here's your {entry}. Enjoy!")
            coffee_machine()
        else:
            coffee_machine()


coffee_machine()
