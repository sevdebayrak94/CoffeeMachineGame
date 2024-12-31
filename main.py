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


def coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?:")) * (0.25)
    dimes = int(input("How many dimes?:")) * (0.1)
    nickles = int(input("How many nickles?:")) * (0.05)
    pennies = int(input("How many pennies?:")) * (0.01)
    top = quarters + dimes + nickles + pennies
    return round(top,2)


def money_check(drink):
    your_money = coins()
    drink_cost = MENU[drink]["cost"]
    if your_money > drink_cost :
        returned_money = your_money - drink_cost
        print(f"Returned Money ${returned_money}")
    else:
        print(f"Sorry not enough money, here is your money ${your_money:.2%} returned...")
        return False

def remaining_resources(drink):
    if money_check(drink) != 0:
        resources["water"] -= MENU[drink]["ingredients"]["water"]
        resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
        if drink == "espresso":
            resources["milk"] = resources["milk"]
        else:
            resources["milk"] -= MENU[drink]["ingredients"]["milk"]

        #print(f"Water: {resources["water"]}\nMilk:{resources["milk"]}\nCoffee:{resources["coffee"]}")
        return resources
    else:
        return 0

game = True
while game:
    user_input = input("What would you like to drink (espresso/latte/cappuccino):")
    if user_input == "report":
        print(f"Water: {resources["water"]}\nMilk:{resources["milk"]}\nCoffee:{resources["coffee"]}")
    else:
        cc = remaining_resources(user_input)
        #print(f"Water: {cc["water"]}\nMilk:{cc["milk"]}\nCoffee:{cc["coffee"]}")
        if cc["water"] < 0:
            print("sorry not enough resources....")
            game = False





