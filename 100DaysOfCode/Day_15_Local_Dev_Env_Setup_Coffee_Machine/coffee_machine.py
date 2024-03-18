# TODO Copy MENU and resources to a separate file. Then, import them into your program.
# TODO Ask the user to select a type of coffee.
# TODO For maintenance, select "Maintenance". To print a report of resources, select "Print Resource Report".
# TODO Check if there are enough resources to make the selected coffee. If so, the program should warn the user.
# TODO If there are enough resources, ask the user to insert coins.
# TODO Once the user has entered all coins, check if there is enough money to pay for the selected coffee.
# TODO If there's not enough money, program should warn the user that there are insufficient funds and that it'll be refunded.
# TODO If there are enough resources and money, deliver the coffee.
# TODO The program should stop only when there is not enough resources, money, or the word "off" is selected.
from menu_resources import *


def report():
    water_available = resources['water']
    milk_available = resources['milk']
    coffee_available = resources['coffee']

    print('\nSummary')
    print(f'Water   : {water_available} ml')
    print(f'Milk    : {milk_available} ml')
    print(f'Coffee  : {coffee_available} gr')
    print(f'Money   : {money} $\n')


def resources_check(user_choice):
    water_needed = MENU[user_choice]["ingredients"]["water"]

    if user_choice == 'espresso':
        milk_needed = 0
    else:
        milk_needed = MENU[user_choice]["ingredients"]["milk"]

    coffee_needed = MENU[user_choice]["ingredients"]["coffee"]

    if resources['water'] < water_needed:
        print('Sorry there is not enough water.')
    elif resources['milk'] < milk_needed:
        print('Sorry there is not enough milk.')
    elif resources['coffee'] < coffee_needed:
        print('Sorry there is not enough coffee.')
    else:
        print('Resources OK')


money = 0
quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01


machine_off = False
while not machine_off:

    user_choice = input('What would you like? (espresso/latte/cappuccino): ').lower()
    if user_choice == 'off':
        print('Coffee machine turned off')
        machine_off = True
    elif user_choice == 'report':
        report()
    elif user_choice in ('espresso', 'latte', 'cappuccino'):
        resources_check(user_choice)
        print(f'\nYour selection: {user_choice.title()}')
        print(f"Price: {MENU[user_choice]['cost']:.2F} $\n")
        print('Please insert coins')
        quarters_amount = int(input('How many quarters? '))
        dimes_amount = int(input('How many dimes? '))
        nickles_amount = int(input('How many nickles? '))
        pennies_amount = int(input('How many pennies? '))









