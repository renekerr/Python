# Calculator
from art import logo
from mod_clear_screen import clear_screen


def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
print(logo)

def calculator():
  num1 = float(input("Enter the first number?: "))
  should_continue = True
  
  while should_continue:
    operation_symbol = input("Pick an operation (+, -, * or /): ")
    num2 = float(input("Enter another number?: "))

    calculation = operations[operation_symbol](num1,num2) 
    result = calculation

    print(f'{num1} {operation_symbol} {num2} = {result}')

    calculate_again = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, or 'exit' to stop.: ")

    if calculate_again == 'y':
      num1 = result
    elif calculate_again == 'n':
      clear_screen()
      calculator()
    elif calculate_again == 'exit':
      should_continue = False  # Set should_continue to False to exit the loop
      print("Goodbye!")
      break  # Exit the loop
      
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

