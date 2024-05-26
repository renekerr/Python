'''
Create a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:

You have x weeks left.
Where x is replaced with the actual calculated number of weeks the input age has left until age 90.

Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.
'''

age = int(input('Please, enter your age: '))
# Write your code below this line 👇
remaining_years = 90 - age
weeks_in_a_year = 52
weeks_left = remaining_years * weeks_in_a_year
print(f'You have {weeks_left} weeks left.')

