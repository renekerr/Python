# Functions in Python
# A function is a block of code that performs a specified task

##    Python function format   ##
# def function_name (optional_parameters):
#       statement(s)
#       ......
#       ......
# print("not par of the function")

# This function prints "hello there!" when it is called/invoked

def hello():
    print("hello there!")

print("First time invoked!")
hello() # function invoked here
print("")

print("Function called within a for loop")
for k in range(1,4):
    print("k is = ", k)
    hello()