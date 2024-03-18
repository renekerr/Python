import random

def random_number():
    """
    Generates a random number between 1 and 100 (inclusive).

    Returns:
        int: A random integer between 1 and 100.
    """
    generated_number = random.randint(1,100)
    return generated_number

def guess_number(difficulty_level):
    """
    Plays the Number Guessing Game based on the specified difficulty level.

    Args:
        difficulty_level (str): The difficulty level of the game, either 'easy' or 'hard'.

    Returns:
        None
    """
    if difficulty_level == 'hard':
        attempts = 5
    elif difficulty_level == 'easy':
        attempts = 10

    print('-' * 30)
    print(f'Difficulty level: {difficulty_level.title()}')
    print(f'Total attempts: {attempts}\n')
    
    while attempts > 0:
        guess = int(input('Make a guess: '))
        if guess == generated_number: 
            print(f'You got it! The answer was {generated_number}.')
            attempts = 0
        elif guess > generated_number:
            attempts -= 1
            print(f'Too high.')
            if attempts == 0:
                print("You've run out of guesses, you lose.")
            else: 
                print(f"Guess again.\nYou have {attempts} attempts remaining to guess the number.\n")
        elif guess < generated_number:
            attempts -= 1
            print(f'Too low.')
            if attempts == 0:
                print("You've run out of guesses, you lose.")
            else: 
                print(f"Guess again.\nYou have {attempts} attempts remaining to guess the number.\n")  
              

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
generated_number = random_number()
# print(f'Pssst, the correct answer is {generated_number}')
difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
guess_number(difficulty_level)










    




