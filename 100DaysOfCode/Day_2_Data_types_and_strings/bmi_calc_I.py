'''
Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m)
'''

# 1st input: enter height in meters e.g: 1.65
height = input('Enter height in meters: ')
# 2nd input: enter weight in kilograms e.g: 72
weight = input('Enter weight in kilograms: ')

# Write your code below this line 👇
height_to_float = float(height)
weight_int = int(weight)
bmi = weight_int / (height_to_float)**2
print(int(bmi))
