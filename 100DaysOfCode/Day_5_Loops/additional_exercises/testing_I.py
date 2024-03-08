#Password Generator Project
import random
letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols_list = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

psw_list_items = []
password_generated = ''

# generating random letters
random_generated_letters = ''
for l in range(0, nr_letters):
    random_number_for_letters = random.randint(0,len(letters_list)-1)
    randomizing_letters = letters_list[random_number_for_letters]
    random_generated_letters += randomizing_letters
psw_list_items.append(random_generated_letters)
#print(random_generated_letters)

# generating random letters
random_generated_numbers = ''
for nr in range(0, nr_numbers):
    random_number_for_numbers = random.randint(0, len(numbers_list)-1)
    randomizing_numbers = numbers_list[random_number_for_numbers]
    random_generated_numbers += randomizing_numbers
psw_list_items.append(random_generated_numbers)
#print(random_generated_numbers)

# generating random symbols
random_generated_symbols = ''
for s in range(0, nr_symbols):
    random_number_for_symbols = random.randint(0, len(symbols_list)-1)
    randomizing_symbols = symbols_list[random_number_for_symbols]
    random_generated_symbols += randomizing_symbols
psw_list_items.append(random_generated_symbols)
print(random_generated_symbols)
password_generated = random_generated_letters + random_generated_symbols + random_generated_numbers

print(f'Eazy password generated (ordered): {password_generated}')

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P





