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
    "milk": 20,
    "coffee": 10,
}


user_selection = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()
if user_selection in ('espresso', 'latte', 'cappuccino'):
    selected_drink = MENU[user_selection]
    ingredients = selected_drink['ingredients']
    print(selected_drink)
    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f'Error. Not enough {item}')

