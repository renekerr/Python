'''

'''

print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
small_pizza = 15
medium_pizza = 20
large_pizza = 25
bill = 0

if size == 'S':
  bill = small_pizza
  if add_pepperoni == 'Y':
    bill = small_pizza + 2
  if extra_cheese == 'Y':
    bill += 1
elif size == 'M':
  bill = medium_pizza
  if add_pepperoni == 'Y':
    bill += 3
  if extra_cheese == 'Y':
    bill += 1
else: 
  bill = large_pizza
  if add_pepperoni == 'Y':
    bill += 3
  if extra_cheese == 'Y':
    bill += 1

print (f'Your final bill is: ${bill}.')

'''
print("Thank you for choosing Python Pizza Deliveries!")
size = input()  # What size pizza do you want? "S", "M", or "L"
add_pepperoni = input()  # Do you want pepperoni? "Y" or "N"
extra_cheese = input()  # Do you want extra cheese? "Y" or "N"

# Your code below this line 👇
bill = 0
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is: ${bill}.")
'''
  
  


