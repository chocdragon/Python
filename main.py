# This is a code for a Drink Machine menu that serves coffee, tea and chocolate milk.

MENU = {
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
    },
    "milk tea": {
        "ingredients": {
            "water": 100,
            "milk": 20,
            "tea": 20,
        },
        "cost": 1.5,
    },
    "hot chocolate": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "cocoa powder": 100,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 800,
    "milk": 500,
    "coffee": 100,
    "tea": 100,
    "cocoa powder": 500,
}

# TODO 4 Check enough resources to make the requested drink
def check_resources(ingredients):
    for item in ingredients:
        if ingredients[item] < resources[item]:
            return True
        else:
            print(f"There is not enough {item}")
            return False


# TODO 5 Process coins
def process_coins(cost):
    global earned
    print(f"Your drink costs ${cost}")
    collection = int(input("How many quarters?: ")) * 0.25
    collection += int(input("How many dimes?: ")) * 0.1
    collection += int(input("How many nickels?: ")) * 0.05
    collection += int(input("How many pennies?: ")) * 0.01
    print(f"Money collected is ${round(collection, 2)}")

# TODO 6 Transaction check
    if collection > cost:
        change = collection - cost
        print(f"Here is ${round(change, 2)} in change.")
        earned = cost
        return True, earned
    else:
        print("You did not provide enough coins. Money refunded.")
        return False


# TODO 7 Make drink will calculate remaining resources after drink is made
def make_drink(choice, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]  # Deduct ingredients from the main resources
    print(f"Enjoy your {choice}.")

is_on = True
profit = float(0.0)

# TODO 1 Customer prompt
while is_on:
    print(" *** Latte $2.50 | Cappuccino $3.00 | Milk Tea $1.50 | Hot Chocolate $3.00 *** ")
    user_choice = (input("What would you like? (Latte, Cappuccino, Milk Tea, Hot Chocolate): ")).lower()

# TODO 2 Turn off machine by service technician
    if user_choice == "off":
        print(" >>> It is now safe to turn off the machine. <<< ")
        is_on = False
# TODO 3 Show report for service technician
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Tea: {resources['tea']}g")
        print(f"Cocoa Powder: {resources['cocoa powder']}g")
        print(f"Profit: ${profit}")
    else:
        drink = MENU[user_choice]
        if drink:
            if check_resources(drink['ingredients']):
                if process_coins(drink['cost']):
                    profit += earned
                    make_drink(user_choice, drink['ingredients'])
            else:
                is_on = False
        else:
            print("Invalid option.")
