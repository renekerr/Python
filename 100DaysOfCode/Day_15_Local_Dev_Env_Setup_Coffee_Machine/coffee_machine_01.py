# TODO Copy MENU and resources to a separate file. Then, import them into your program.
# TODO Ask the user to select a type of coffee.
# TODO For maintenance, select "Maintenance". To print a report of resources, select "Print Resource Report".
# TODO Check if there are enough resources to make the selected coffee. If so, the program should warn the user.
# TODO If there are enough resources, ask the user to insert coins.
# TODO Once the user has entered all coins, check if there is enough money to pay for the selected coffee.

# TODO If there's not enough money, program should warn the user that there are insufficient funds
#  and that it'll be refunded.

# TODO If there are enough resources and money, deliver the coffee.
# TODO The program should stop only when there is not enough resources, money, or the word "off" is selected.
from menu_resources import *


def resources_update(water, milk, coffee):
    """Update available resources by subtracting given amounts of water, milk, and coffee."""
    resources['water'] -= water
    resources['milk'] -= milk
    resources['coffee'] -= coffee
    return resources['water'], resources['milk'], resources['coffee']


def print_report(curr_w, curr_m, curr_c, curr_cash):
    """Print a summary report of current resources and cash."""
    print('\nSummary')
    print(f'\tWater   : {curr_w} ml')
    print(f'\tMilk    : {curr_m} ml')
    print(f'\tCoffee  : {curr_c} gr')
    print(f'\tMoney   : {curr_cash:.2F} $')


def resources_check(user_choice):
    """Check if there are enough resources to make the selected user choice."""
    resources_output = True
    water_needed = MENU[user_choice]["ingredients"]["water"]

    if user_choice == 'espresso':
        milk_needed = 0
    else:
        milk_needed = MENU[user_choice]["ingredients"]["milk"]

    coffee_needed = MENU[user_choice]["ingredients"]["coffee"]

    if resources['water'] < water_needed:
        print('Sorry there is not enough water.')
        resources_output = False
        return resources_output
    elif resources['milk'] < milk_needed:
        print('Sorry there is not enough milk.')
        resources_output = False
        return resources_output
    elif resources['coffee'] < coffee_needed:
        print('Sorry there is not enough coffee.')
        resources_output = False
        return resources_output
    else:
        # Resources OK
        resources_output = True
        return resources_output


def money_provided_sum(quarters_in, dimes_in, nickles_in, pennies_in):
    """Calculate the total sum of money provided based on the number of quarters, dimes, nickels, and pennies."""
    total_sum = quarters_in * 0.25 + dimes_in * 0.10 + nickles_in * 0.05 + pennies_in * 0.01
    print(f'\nTotal money entered: {total_sum:.2F} $')
    return total_sum


def transaction_validation(total_cash, cost, selection):
    """Validate the transaction based on the total cash, cost, and coffee selection."""
    coffee_delivered = False

    if total_cash >= cost:
        print('Preparing your coffee and your change...please wait!')
        change_amount = total_cash - cost
        print(f'Here is your {selection}. Enjoy!.')
        print(f'Change: {change_amount:.2F} $')
        coffee_delivered = True
        return coffee_delivered
    else:
        print("Sorry that's not enough money. Money refunded.")


def coffee_machine():
    """Simulate the operation of a coffee machine."""
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
            w, m, c = resources_update(water=water_used, milk=milk_used, coffee=coffee_used)
            print_report(curr_w=w, curr_m=m, curr_c=c, curr_cash=cash)
        elif user_selection in ('espresso', 'latte', 'cappuccino'):
            resource_flag = resources_check(user_choice=user_selection)

            if resource_flag:
                coffee_cost = MENU[user_selection]['cost']
                print(f'\nYour selection: {user_selection.title()}')
                print(f"Price: {coffee_cost:.2F} $\n")

                print('Please insert coins')
                quarters_entered = int(input('\tHow many quarters? '))
                dimes_entered = int(input('\tHow many dimes? '))
                nickles_entered = int(input('\tHow many nickles? '))
                pennies_entered = int(input('\tHow many pennies? '))

                total_cash_entered = money_provided_sum(quarters_in=quarters_entered, dimes_in=dimes_entered,
                                                        nickles_in=nickles_entered, pennies_in=pennies_entered)

                trans_success = transaction_validation(total_cash=total_cash_entered, cost=coffee_cost,
                                                       selection=user_selection)

                if trans_success:
                    # Update resource after coffee has been delivered
                    cash += coffee_cost
                    water_used = MENU[user_selection]["ingredients"]["water"]

                    if user_selection == 'espresso':
                        milk_used = 0
                    else:
                        milk_used = MENU[user_selection]["ingredients"]["milk"]

                    coffee_used = MENU[user_selection]["ingredients"]["coffee"]


coffee_machine()
