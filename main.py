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



# TODO: 2. Turn off the Coffee Machine by entering “ off ” to the prompt.

# TODO: 3. Print report.
money = 0
total_amt_user = 0
cost = 0
change = 0
transaction_success = ""
should_continue = True
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]

while should_continue:

    # TODO: 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
    user = input("What would you like? (espresso/latte/cappuccino) : ").lower()
    if user == "report":
        print(f"Water: {water}ml \nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")
        user = input("What would you like? (espresso/latte/cappuccino) : ").lower()

    # TODO: 4. Check resources sufficient?


    if user == "espresso":
        if water < 50:
            print("Sorry, there is not enough water.")
            should_continue = False
        elif coffee < 18:
             print("Sorry, there is not enough coffee.")
             should_continue = False
    elif user == "latte":
        if water < 200:
             print("Sorry, there is not enough water.")
             should_continue = False
        elif milk < 150:
             print("Sorry, there is not enough milk.")
             should_continue = False
        elif coffee < 24:
             print("Sorry, there is not enough coffee.")
             should_continue = False
    elif user == "cappuccino":
        if water < 250:
             print("Sorry, there is not enough water.")
             should_continue = False
        elif milk < 100:
             print("Sorry, there is not enough milk.")
             should_continue = False
        elif coffee < 24:
             print("Sorry, there is not enough coffee.")
             should_continue = False




    # TODO: 5. Process coins.
    if should_continue == True:
        if user == "espresso":
            c = 1.5
        elif user == "latte":
            c = 2.5
        elif user == "cappuccino":
            c = 3.0
        print(f"Cost of {user} is {c}")
        print("Please insert coins.")
        no_quarters = int(input("How many quarters?: "))
        no_dimes = int(input("How many dimes?: "))
        no_nickles = int(input("How many nickles?: "))
        no_pennies = int(input("How many pennies?: "))

    def process_coins():
        return round((no_quarters * 0.25) + (no_dimes * 0.10) + (no_nickles * 0.05) + (no_pennies * 0.01), 2)
        # print(f"${total_amt_user}")


    # TODO: 6. Check transaction successful?
    def transaction(uservalue):
        if user == "espresso":
            cost_coffee = 1.5
            return cost_coffee
        elif user == "latte":
            cost_coffee = 2.5
            return cost_coffee
        elif user == "cappuccino":
            cost_coffee = 3.0
            return cost_coffee

    if should_continue == True:
        cost = transaction(user)
        money += cost
        amt = process_coins()
        if amt >= cost:
            transaction_success = "yes"
        else:
            transaction_success = "no"

        if amt > cost:
            change = round((amt - cost), 2)
            print(f"Here is ${change} in change.")
        elif amt < cost:
            print("Sorry, that's not enough money. Money refunded.")
            should_continue = False

    # TODO: 7. Make Coffee.

        if user == "espresso":
            water -= 50
            coffee -= 18
        elif user == "latte":
            water -= 200
            milk -= 150
            coffee -= 24
        elif user == "cappuccino":
            water -= 250
            milk -= 100
            coffee -= 24
        print(f"Here is your {user} enjoy.")





