# Create a calculator class.
# Include methods for basic arithmetic operations.

class Calculator:
    """
    This class performs basic mathematical calculations.
    """
    def add(self, value1, value2):
        return value1 + value2

    def subtract(self, value1, value2):
        return value1 - value2

    def multiply(self, value1, value2):
        return value1 * value2

    def divide(self, value1, value2):
        if value2 == 0:
            return 'Division by zero is not allowed.'
        return value1 / value2


calc = Calculator()


print("Welcome to the Simple Calculator!")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Choose operation (+, -, *, /):")

if operation == '+':
    result = calc.add(num1, num2)
elif operation == '-':
    result = calc.subtract(num1, num2)
elif operation == '*':
    result = calc.multiply(num1, num2)
elif operation == '/':
    result = calc.divide(num1, num2)

print(f"{num1} {operation} {num2} = {result}")
