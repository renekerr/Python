# Import the random library.
from random import choice
from game_data import data

# Create a function to generate random item from data list
def get_random_item():
    return choice(data)

# Create a function to compare followers from A and B

# Get items (for A and B) from the data (list) using the choice() function from the random library. A and B have to be different. 
a = {}
b = {}
score = 0
while a == b:
    a = get_random_item()
    b = get_random_item()

# Once both are chosen, print them using this pattern: name, description, and country.
print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}, with {a['follower_count']} followers.")
print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}, with {b['follower_count']} followers.")

# Ask user to guess who's got more followers
user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()



# Once compared, if comparison is correct, the one with less followers should be removed from list.

# Create a variable to accumulate the score, which should be set to 0 initially.

# If the comparison is correct, increase the score by 1 and set B as A. Then, generate a new B randomly.

# If the comparison is not correct, the program should finish, and the final score should be printed.

# Use a while loop to continually compare A against B until the user gets it wrong.

