'''
Instructions
Read this the code in main.py
Spot the problems 🐞.
Modify the code to fix the program.
No shortcuts - don't copy-paste to replace the code entirely with a working solution.
Fix the code so that it works and when you hit submit it should pass all the tests.


# Which year do you want to check?
year = input('Enter a year: ')

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")

Error: 
    if year % 4 == 0:
    
TypeError: not all arguments converted during string formatting

Poblem
Variable year is a string not an integer value

Solution
Convert year to int
'''

# Solution
# Which year do you want to check?
year = int(input('Enter a year: '))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")