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

money = 0

def check_resources(drink):
    """Determine if sufficient resources exist to make the requested drink"""

    sufficient = True

    for ingredient in MENU[drink]["ingredients"]:
        if resources[ingredient] < MENU[drink]["ingredients"][ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            sufficient = False
            break
    return sufficient

def vend(drink):
    """Carry out the sale of the specified drink, returns amount paid"""

    global resources

    print("Please insert coins.")

    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))

    amount_paid = .25 * quarters + .1 * dimes + .05 * nickels + .01 * pennies
    price = MENU[drink]["cost"]

    if amount_paid < price:
        print("Sorry, that's not enough money. Money refunded.")
        return 0
    else:
        # Decrement resources needed
        for resource in MENU[drink]["ingredients"]:
            amount_needed = MENU[drink]["ingredients"][resource]
            resources[resource] -= amount_needed

        # Dispense change and drink
        change = "{:.2f}".format(amount_paid - price)
        print(f"Here is ${change} in change.")
        print(f"Here is your {drink} ☕️. Enjoy!")

        return price

while True:
    selection = input("What would you like? (espresso/latte/cappuccino): ")
    match selection:
        case "off":
            break;
        case "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${'{:.2f}'.format(money)}")
        case "espresso":
            if check_resources("espresso"):
                money += vend("espresso")
        case "latte":
            if check_resources("latte"):
                money += vend("latte")
        case "cappuccino":
            if check_resources("cappuccino"):
                money += vend("cappuccino")
        case _:
            print("Selection invalid. Try again.")