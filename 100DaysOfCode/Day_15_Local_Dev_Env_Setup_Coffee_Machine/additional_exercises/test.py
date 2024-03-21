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

COINS = {'quarters': 0.25, 'dimes': 0.1, 'nickels': 0.05, 'pennies': 0.01}


total_money = 0
print('Insert coins, please.')
for k, v in COINS.items():
    coins = int(input(f'\tHow many {k}? '))
    total_money += coins * v

print(f'{total_money:.2F}')


# user_selection = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()
# if user_selection in ('espresso', 'latte', 'cappuccino'):
#     selected_drink = MENU[user_selection]
#     ingredients = selected_drink['ingredients']
#     items_depleted = []
#     for item in ingredients:
#         if resources[item] < ingredients[item]:
#             items_depleted.append(item)
#
#     for i in items_depleted:
#         print(f'Insufficient {i}')
#     print('Error: Coffee ingredients depleted. Unable to serve.')




