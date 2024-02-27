# Functions Exercise 9 (Evaluate an Expression)
# This program evaluate x on the expression below
# y = x^4 - 12x^3 + 13x^2 + 11

def calc_expresion(x):
    y = (x**4) - 12*(x**3) + 13*(x**2) + 11
    return y


# Main program
user_response = input("Enter the value(integer) of x : ")
x = int(user_response)


m = calc_expresion(x)

print("When x is", x, ", the expresion x^4 - 12x^3 + 13x^2 + 11 = ", m)