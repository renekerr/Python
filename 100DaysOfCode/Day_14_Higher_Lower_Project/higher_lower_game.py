# Import the random library.
from random import choice
from game_data import data

# Create a function to generate random item from data list.
def get_random_item():
    '''
    Generate a random item from the provided data list.
    '''
    return choice(data)

# Create a function that compare A and B followers and return who's got more followers.
def compare_followers(followers_a, followers_b):
    """
    Compare the number of followers for two entities and return who has more followers.

    Parameters:
    followers_a (int): The number of followers for entity A.
    followers_b (int): The number of followers for entity B.

    Returns:
    str: 'a' if entity A has more followers, 'b' if entity B has more followers,
         or 'equal' if both entities have the same number of followers.
    """
    if followers_a > followers_b:
        return 'a'
    elif followers_b > followers_a:
        return 'b'
    else:
        return 'equal'

# Create a function that compares user guess with entity that has more followers
def compare_user_guess(user_guess, higher_follower, score):
    '''
    Compares user's guess with entity with higher followers
    '''
    correct_answer = False
    if user_guess == higher_follower:
        print(f'Correct answer. Current score: {score + 1}')
        correct_answer = True
        return correct_answer
    else:
        print(f'Incorrect answer. Final score: {score}')


# Create a variable to accumulate the score, which should be set to 0 initially.
score = 0

# Create empty lists for A and B
a = {}
b = {}



# Get items (for A and B) from the data (list) using the choice() function from the random library. A and B have to be different. 
while a == b:
    a = get_random_item()
    b = get_random_item()

# Once both are chosen, print them using this pattern: name, description, and country.
print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}, with {a['follower_count']} followers.")
print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}, with {b['follower_count']} followers.")

higher_follower = compare_followers(a['follower_count'], b['follower_count'])

# Ask user to guess who's got more followers
user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

compare_user_guess(user_guess, higher_follower, score)



# Once compared, if comparison is correct, A should be removed from list.

# If the comparison is correct, increase the score by 1 and set B as A. Then, generate a new B randomly.

# If the comparison is not correct, the program should finish, and the final score should be printed.

# Use a while loop to continually compare A against B until the user gets it wrong.

