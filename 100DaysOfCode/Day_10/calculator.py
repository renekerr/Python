# Calculator
from art import logo
print(logo)

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

result = 0
accumulated = 0
continue_calc = False
operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

# First number
num1 = int(input("What's the first number?: "))

# Operations
for key, value in operations.items():
  print(key)

operation_symbol = input("Pick an operation from the line above: ")

# Second number
num2 = int(input("What's the second number?: "))

# Calculation and result
calculation = operations[operation_symbol](num1,num2)
first_result = calculation

# Printing out the result (first)
print(f'{num1} {operation_symbol} {num2} = {first_result}')
calculate_again = input(f"Type 'y' to continue calculating with {first_result}, or type 'n' to exit.: ")

operation_symbol = input("Pick another operation (+, -, * or /): ")
num3 = int(input("What's the next number?: "))
calculation = operations[operation_symbol](first_result, num3)
second_result = calculation

# Printing out the result (second)
print(f'{first_result} {operation_symbol} {num3} = {second_result}')









'''
# Calculation and result
# Another way is:

calculation = operations[operation_symbol]
result = calculation(num1,num2)
'''



# if operation_symbol == '+':
#   result = add(num1, num2)
# elif operation_symbol == '-':
#   result = subtract(num1, num2)
# elif operation_symbol == '*':
#   result = multiply(num1, num2)
# elif operation_symbol == '/':
#   result = divide(num1, num2)

