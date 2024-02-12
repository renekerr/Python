# Making Calculations from User Input with Python
# Converting from Fahrenheit to Celsius
f = float(input("What temperature (in Fahrenheit) would you like to convert to Celsius? "))
c = (f - 32) * 5 / 9
print(f, "F is ", round(c, 2), "Cº")
