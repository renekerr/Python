from menu_resources import *


def check_resources(user_choice):
    resources_output = True
    water_needed = MENU[user_choice]["ingredients"]["water"]

    if user_choice == 'espresso':
        milk_needed = 0
    else:
        milk_needed = MENU[user_choice]["ingredients"]["milk"]

    coffee_needed = MENU[user_choice]["ingredients"]["coffee"]

    for ingredient, value in MENU[user_selection]["ingredients"].items():
        if resources[ingredient] < value:
            print(f'Sorry, there is not enough {ingredient}.')
            resources_output = False
        else:
            return resources_output


user_selection = input('\nWhat would you like? (espresso/latte/cappuccino): ').lower()