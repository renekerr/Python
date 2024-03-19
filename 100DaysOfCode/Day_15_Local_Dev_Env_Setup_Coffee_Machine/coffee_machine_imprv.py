from menu_resources import *

# Constants
COIN_VALUES = {'quarters': 0.25, 'dimes': 0.10, 'nickels': 0.05, 'pennies': 0.01}


def update_resources(water, milk, coffee):
    """Update the resources after serving a drink."""
    resources['water'] -= water
    resources['milk'] -= milk
    resources['coffee'] -= coffee
    return resources['water'], resources['milk'], resources['coffee']


def print_report(curr_w, curr_m, curr_c, curr_cash):
    """Print the current resources report."""
    print('\nSummary')
    print(f'\tWater   : {curr_w} ml')
    print(f'\tMilk    : {curr_m} ml')
    print(f'\tCoffee  : {curr_c} gr')
    print(f'\tMoney   : {curr_cash} $')


def check_resources(user_choice):
    """Check if there are enough resources to make the selected drink."""
    resources_output = True

    water_needed = MENU[user_choice]["ingredients"]["water"]
    milk_needed = MENU[user_choice]["ingredients"].get("milk", 0)  # Default to 0 if milk is not specified (if
    # user_selection equal to espresso
    coffee_needed = MENU[user_choice]["ingredients"]["coffee"]

    for ingredient, value in MENU[user_selection]["ingredients"].items():
        if resources[ingredient] < value:
            print(f'Sorry, there is not enough {ingredient}.')
            resources_output = False
        else:
            return resources_output


def money_provided_sum(quarters_in, dimes_in, nickles_in, pennies_in):
    total_sum = quarters_in * 0.25 + dimes_in * 0.10 + nickles_in * 0.05 + pennies_in * 0.01
    print(f'\nTotal money entered: {total_sum:.2F} $')
    return total_sum


def transaction_validation(total_cash, cost, selection):
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


water_used = 0
milk_used = 0
coffee_used = 0
cash = 0
machine_off = False
while not machine_off:

    user_selection = input('\nWhat would you like? (espresso/latte/cappuccino): ').lower()

    if user_selection == 'off':
        print('Coffee machine has been turned OFF.')
        machine_off = True
    elif user_selection == 'report':
        w, m, c = update_resources(water=water_used, milk=milk_used, coffee=coffee_used)
        print_report(curr_w=w, curr_m=m, curr_c=c, curr_cash=cash)
    elif user_selection in ('espresso', 'latte', 'cappuccino'):
        resource_flag = check_resources(user_choice=user_selection)

        if resource_flag:
            coffee_cost = MENU[user_selection]['cost']
            print(f'\nYour selection: {user_selection.title()}')
            print(f"Price: {coffee_cost:.2F} $\n")

            print('Please insert coins')
            quarters_entered = int(input('\tHow many quarters? '))
            dimes_entered = int(input('\tHow many dimes? '))
            nickles_entered = int(input('\tHow many nickles? '))
            pennies_entered = int(input('\tHow many pennies? '))
            total_cash_entered = money_provided_sum(quarters_in=quarters_entered, dimes_in=dimes_entered, nickles_in=nickles_entered, pennies_in=pennies_entered)

            transaction_success = transaction_validation(total_cash=total_cash_entered, cost=coffee_cost, selection=user_selection)

            if transaction_success:
                # Resources update
                cash += coffee_cost
                water_used = MENU[user_selection]["ingredients"]["water"]

                if user_selection == 'espresso':
                    milk_used = 0
                else:
                    milk_used = MENU[user_selection]["ingredients"]["milk"]

                coffee_used = MENU[user_selection]["ingredients"]["coffee"]
















