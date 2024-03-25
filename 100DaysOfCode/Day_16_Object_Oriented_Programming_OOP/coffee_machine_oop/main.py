from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


print('\nCoffee machine status: ON')
machine_on = True
while machine_on:
    choice = input(f"\nWhat would you like? ({menu.get_items()}): ").lower()
    if choice == 'off':
        print('\nCoffee machine status: OFF')
        machine_on = False
    elif choice == "report":
        print('\nReport')
        coffee_maker.report()
        money_machine.report()
    elif choice in ('espresso', 'latte', 'cappuccino'):
        drink = menu.find_drink(choice)
        print(f'\nYour selection : {choice.title()}')
        print(f'Price : {drink.cost} $\n')
        if coffee_maker.is_resource_sufficient(drink):
            payment = money_machine.make_payment(drink.cost)
            if payment:
                print('Preparing your coffee, please wait...')

    else:
        print('Error. Make sure you enter a valid drink.')

