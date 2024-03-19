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


def report_updated(water, milk, coffee, earnings):
    return water, milk, coffee, earnings


def print_report(water_count, milk_count, coffee_count, money_count):
    print('\nSummary')
    print(f'Water   : {water_count} ml')
    print(f'Milk    : {milk_count} ml')
    print(f'Coffee  : {coffee_count} gr')
    print(f'Money   : {money_count} $\n')


def resources_check(user_selection):
    water_needed = MENU[user_selection]["ingredients"]["water"]

    if user_selection == 'espresso':
        milk_needed = 0
    else:
        milk_needed = MENU[user_selection]["ingredients"]["milk"]

    coffee_needed = MENU[user_selection]["ingredients"]["coffee"]

    if resources['water'] < water_needed:
        print('Sorry there is not enough water.')
    elif resources['milk'] < milk_needed:
        print('Sorry there is not enough milk.')
    elif resources['coffee'] < coffee_needed:
        print('Sorry there is not enough coffee.')
    else:
        print('Resources OK')


def money_provided_sum(quarters_in, dimes_in, nickles_in, pennies_in):
    total_sum = quarters_in * 0.25 + dimes_in * 0.10 + nickles_in * 0.05 + pennies_in * 0.01
    print(f'\nTotal money entered: {total_sum:.2F} $')
    return total_sum


def money_validation(total_cash, cost, selection):
    coffee_delivered = False
    if total_cash >= cost:
        print('Preparing your coffee and your change...please wait!')
        change_amount = total_cash - cost
        print(f'Here is your {selection}.')
        print(f'Change: {change_amount:.2F} $')
        coffee_delivered = True
        return coffee_delivered
    else:
        print("Sorry that's not enough money. Money refunded.")


benefits = 0
machine_off = False
while not machine_off:

    user_choice = input('\nWhat would you like? (espresso/latte/cappuccino): ').lower()

    if user_choice == 'off':
        print('Coffee machine turned off')
        machine_off = True
    elif user_choice == 'report':
        w, m, c, e = report_updated(water=resources['water'], milk=resources['milk'], coffee=resources['coffee'], earnings=benefits)
        print_report(w, m, c, e)
    elif user_choice in ('espresso', 'latte', 'cappuccino'):
        resources_check(user_choice)
        coffee_cost = MENU[user_choice]['cost']
        print(f'\nYour selection: {user_choice.title()}')
        print(f"Price: {coffee_cost:.2F} $\n")

        print('Please insert coins')
        quarters_entered = int(input('\tHow many quarters? '))
        dimes_entered = int(input('\tHow many dimes? '))
        nickles_entered = int(input('\tHow many nickles? '))
        pennies_entered = int(input('\tHow many pennies? '))

        total_money = money_provided_sum(quarters_entered, dimes_entered, nickles_entered, pennies_entered)
        product_delivered = money_validation(total_money, coffee_cost, user_choice)

        if product_delivered:
            update_water = MENU[user_choice]["ingredients"]["water"] - resources['water']
            update_milk = MENU[user_choice]["ingredients"]["milk"] - resources['milk']
            update_coffee = MENU[user_choice]["ingredients"]["coffee"] - resources['coffee']
            update_benefits = benefits + coffee_cost
            report_updated(update_water, update_milk, update_coffee, update_benefits)













