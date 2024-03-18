import random

def random_number():
    '''
    Generates and returns a random number between 1 and 100 including both endpoints.

    Returns:
        int: A random integer
    '''
    num = random.randint(1,100)
    return num

def hard():
    attempts = 5
    print(f'You have {attempts} attempts remaining to guess the number.')
    while attempts > 0:
        guess = int(input('Make a guess: '))
        if guess == n: 
            print(f'You got it! The answer was {n}.')
            attempts = 0
        elif guess > n:
            attempts -= 1
            print(f'Too high.')
            if attempts == 0:
                print("You've run out of guesses, you lose.")
            else: 
                print(f"Guess again.\nYou have {attempts} attempts remaining to guess the number.")
        elif guess < n:
            attempts -= 1
            print(f'Too low.')
            if attempts == 0:
                print("You've run out of guesses, you lose.")
            else: 
                print(f"Guess again.\nYou have {attempts} attempts remaining to guess the number.")

def easy():
    attempts = 10
    print(f'You have {attempts} attempts remaining to guess the number.')
    while attempts > 0:
        guess = int(input('Make a guess: '))
        if guess == n: 
            print(f'You got it! The answer was {n}.')
            attempts = 0
        elif guess > n:
            attempts -= 1
            print(f'Too high.')
            if attempts == 0:
                print("You've run out of guesses, you lose.")
            else: 
                print(f"Guess again.\nYou have {attempts} attempts remaining to guess the number.")
        elif guess < n:
            attempts -= 1
            print(f'Too low.')
            if attempts == 0:
                print("You've run out of guesses, you lose.")
            else: 
                print(f"Guess again.\nYou have {attempts} attempts remaining to guess the number.")
       

n = random_number()
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
print(f'Pssst, the correct answer is {n}')
level = input("Choose a difficulty. Type 'easy' or 'hard': ")

if level == 'hard':
    hard()
elif level == 'easy':
    easy()







    




