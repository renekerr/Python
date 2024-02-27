# This function prints "hello there!" when it is called/invoked

def hello(input_string):
    print("Your input string is: ", input_string)

print("Function called within a for loop")
user_str = input("Enter a string: ")

for k in range(1,4):
    print("k is = ", k)
    hello(user_str)
