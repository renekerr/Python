# TODO Copy MENU and resources to a separate file. Then, import them into your program.
# TODO Ask the user to select a type of coffee.
# TODO For maintenance, select "Maintenance". To print a report of resources, select "Print Resource Report".
# TODO Check if there are enough resources to make the selected coffee. If so, the program should warn the user.
# TODO If there are enough resources, ask the user to insert coins.
# TODO Once the user has entered all coins, check if there is enough money to pay for the selected coffee.
# TODO If there's not enough money, program should warn the user that there are insufficient funds and that it'll be refunded.
# TODO If there are enough resources and money, deliver the coffee.
# TODO The program should stop only when there is not enough resources, money, or the word "off" is selected.

"""
Prices:
    Espresso    : 1.50
    Latte       : 2.50
    Cappuccino  : 3.00
"""
from menu_resources import *


def report():
    water_available = resources['water']
    milk_available = resources['milk']
    coffee_available = resources['coffee']

    print(f'Water   : {water_available} ml')
    print(f'Milk    : {milk_available} ml')
    print(f'Coffee  : {coffee_available} gr')
    print(f'Money   : {money} $')


money = 0
# user_choice = input('What would you like? (espresso/latte/cappuccino): ').lower()
user_choice = 'latte'
print(f'Your selection: {user_choice.title()}')
print(f"Price: {MENU[user_choice]['cost']:.2F} $")

# Compare selection against resources
for k, v in MENU[user_choice]['ingredients'].items():
    print(k, v)

for i, j in resources.items():
    print(i, j)








