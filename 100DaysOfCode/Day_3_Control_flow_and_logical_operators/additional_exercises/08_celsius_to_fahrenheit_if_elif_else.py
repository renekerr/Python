# This program converts from Celsius to Fahrenheit
user_response = input("Please input the temperature in Celsius: ")

# Since input() function always returns a string, the result should be converted it. See line below
celsius = int(user_response) # use celsius = float(user_response) if the user inputs a floating point number

fahrenheit = ((celsius*9)/5)+32
print("The temperature is", fahrenheit, " degrees Fahrenheit")

# Example of the if elif statement
if fahrenheit < 32 :
    print("It is freezing!")
elif fahrenheit < 50:
    print("It is chilly!")
elif fahrenheit < 90:
    print("It is OK!")   
else :
    print("It is hot!")


