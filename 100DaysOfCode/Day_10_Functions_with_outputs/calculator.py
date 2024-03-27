# Calculator
from mod_exit_program import exit_program
from art import logo
from mod_clear_screen import clear_screen


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0:
        return 'Division by zero is not allowed.'
    return n1 / n2


def perform_calculation(first_number, second_number, operator):
    """Performs a calculation based on the given operator."""
    calculation_result = operations[operator](first_number, second_number)
    return calculation_result


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    print(logo)
    num1 = float(input("Enter the first number?: "))
    should_continue = True

    while should_continue:
        operator = input("Pick an operation (+, -, * or /): ")
        num2 = float(input("Enter another number?: "))

        calculation_result = perform_calculation(num1, num2, operator)

        print(f'{num1} {operator} {num2} = {calculation_result}')

        calculate_again = input(
            f"Type 'y' to continue calculating with {calculation_result}, or type 'n' to start a new calculation, or type 'exit' to quit calculator: ")

        if calculate_again == 'y':
            num1 = calculation_result
        elif calculate_again == 'n':
            clear_screen()
            calculator()
        elif calculate_again == 'exit':
            exit_program()


# Call calculator function
calculator()

'''
# Calculation and result
# Another way is:

calculation = operations[operation_symbol]
result = calculation(num1,num2)
'''

# Operations
# for key, value in operations.items():
#   print(key)


# if operation_symbol == '+':
#   result = add(num1, num2)
# elif operation_symbol == '-':
#   result = subtract(num1, num2)
# elif operation_symbol == '*':
#   result = multiply(num1, num2)
# elif operation_symbol == '/':
#   result = divide(num1, num2)
