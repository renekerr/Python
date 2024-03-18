'''
Day 12 - Namespaces

Namespaces: Are virtual spaces where the names of variables, functions, classes, or other elements are uniquely defined within that space, helping to avoid naming conflicts and organize the code.

Placeholder: It is a temporary value used in code to represent data that will be determined later. It is commonly used to represent unknown or null values or to indicate where the user should enter data in forms.

Local vs Global scope
                                       
'''
# SCOPE
enemies = 1

def increase_enemies_v1():
    enemies = 2 
    print(f'enemies inside the function: {enemies}')

increase_enemies_v1()
print(f'enemies outside the function: {enemies}')


# Local scope
def days_left():
    days = 2
    print(f'You have {days} days left.')

days_left()
# print(f'You have {days} days left.') # NameError: name 'days' is not defined

# Global scope example 1
player_score = 100 # global variable

def scoring_one():
    points = 10 # local variable
    print(f'Value accessed from inside the function {player_score}')

scoring_one()
print(f'Value accessed from outside the function {player_score}')

# Global scope example 2
player_score = 100 # global variable

def game():
    def scoring():
        points = 10 # local variable
        print(f'Value accessed from inside the function {player_score}')
    scoring()   # should be indented and be part of game()

# scoring() # Error: can be accessed from inside game() function 

print(f'Value accessed from outside the function {player_score}')   

# There is no Block Scope
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
  new_enemy = enemies[0]

print(new_enemy) # variable new_enemy can be accessed

# However if this code is part of a function:
game_level = 3
def game_copy():
   enemies = ["Skeleton", "Zombie", "Alien"]
   if game_level < 5:
       new_enemy_copy= enemies[0]

# print(new_enemy_copy) # Error: variable new_enemy_copy cannot be accessed

# Modifying Global Scope
player_score = 1
def increase_enemies():
  global player_score
  player_score += 1
  print(f"enemies inside function: {player_score}")

increase_enemies()
print(f"enemies outside function: {player_score}")

# Global Constants
PI = 3.14159
URL = "https://www.google.com"



