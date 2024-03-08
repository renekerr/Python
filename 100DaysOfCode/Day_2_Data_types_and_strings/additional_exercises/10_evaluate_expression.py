# Write a program that asks the user for an integer 'x' and prints the value of y
# after evaluating the following expression: y=x2−12x+11

user_response = input("Enter a value for x =  ")
x = int(user_response)
y = (x * x)-(12 * x) + 11

print(f"x = {x} and y = {y} for y = (x * x)-(12 * x) + 11", y)

