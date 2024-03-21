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

COINS = {'quarters': 0.25, 'dimes': 0.1, 'nickels': 0.05, 'pennies': 0.01}


def resources_check(drink_ingredients):
    """Verifies if there are sufficient resources available to make the selected drink."""
    items_depleted = []
    for item in drink_ingredients:
        if resources[item] < drink_ingredients[item]:
            items_depleted.append(item)

    if items_depleted:
        print('Error: Unable to serve.')
        for i in items_depleted:
            print(f'Insufficient {i}.')
        return False
    else:
        return True


def calculate_total_money():
    """Calculate total money based on user input of coins."""
    total_money = 0
    print('Insert coins, please.')
    for coin_name, coin_value in COINS.items():
        coins = int(input(f'\tHow many {coin_name}? '))
        total_money += coins * coin_value

    return total_money


earnings = 0
machine_on = True
print('Coffee machine status: ON')
while machine_on:
    user_selection = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()

    if user_selection == 'off':
        print('\nCoffee machine status: OFF')
        machine_on = False
    elif user_selection == 'report':
        print('\nSummary')
        print(f"\tWater    : {resources['water']} ml")
        print(f"\tMilk     : {resources['milk']} ml")
        print(f"\tCoffee   : {resources['coffee']} gr")
        print(f"\tMoney    : {earnings} $")
    elif user_selection in ('espresso', 'latte', 'cappuccino'):
        selected_drink = MENU[user_selection]
        ingredients = selected_drink['ingredients']
        if resources_check(drink_ingredients=ingredients):
            coffee_cost = MENU[user_selection]['cost']
            print(f'\nYour selection: {user_selection.title()}')
            print(f"Price: {coffee_cost:.2F} $\n")
            calculate_total_money()

    else:
        print('Error. Make sure you enter a valid drink.')


# TODO Add Emojis at the end
