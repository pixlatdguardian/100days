import math

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
    "water": 1000,
    "milk": 1000,
    "coffee": 1000,
}


def cust_input():
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "report":
        for key, value in resources.items():
            print(key, value)
        print(money)
        return cust_input()
    elif choice == "off":
        return False
    else:
        return choice


def round_down(n):
    return math.floor(n * 100) / 100


def exchange(response):
    cost = MENU[response]["cost"]
    print(f"The price is ${cost}")
    quarters = .25 * int(input("How many Quarters do you want to enter?"))
    dimes = .1 * int(input("How many Dimes do you want to enter?"))
    nickles = .05 * int(input("How many Nickles do you want to enter?"))
    pennies = .01 * int(input("How many Pennies do you want to enter?"))
    total = round_down(quarters + dimes + nickles + pennies)
#   #print(total)
    if total >= cost:
        print(f"Thank you for the payment. Your change is ${round_down(total - cost)}")
        return True, money + round_down(cost)
    else:
        print("Please enter the correct amount for the drink. Money Refunded")
        return False, money  # Ensure it always returns a tuple



def check_resources(response):
    drink_res = MENU[response]["ingredients"]
    for key in drink_res:
        if resources[key] < drink_res[key]:
            print(f"Sorry, there is not enough {key}.")
            return False
    return True


def return_drink(drink):
    drink_res = MENU[drink]["ingredients"]
    for key in drink_res:
        resources[key] -= drink_res[key]


money = 0
while True:
    response = cust_input()
    if not response:
        break
    make_drink = check_resources(response)
    if make_drink:
        paid, money = exchange(response)
        return_drink(response)
        print(f"Here is your {response}. Come again soon!")
    else:
        print("Sorry, the machine is out of resources. You are refunded")
        break
