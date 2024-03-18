
from random import randint

EASY_LEVEL_TRIES = 10
HARD_LEVEL_TRIES = 5

def difficult_level(level):
    
    if level == 'hard':
        return HARD_LEVEL_TRIES
    elif level == 'easy':
        return EASY_LEVEL_TRIES
    else: 
        return "Make sure you enter 'hard' or 'easy' as level"

def compare_numbers(guess, generated_number, tries):
    if guess > generated_number:
        print('Too high.')
        return tries - 1 
    elif guess < generated_number:
        print('Too low.')
        return tries - 1
    else:
        print(f'You got it. The correct number is {generated_number}')
        
def play_game():
    print("\nWelcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\n")
    generated_number = randint(1,100)
    print(f'Pssst, the correct answer is {generated_number}\n')
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    tries = difficult_level(level)
    print(f'\nDifficulty level: {level.capitalize()}')
    print(f'Total attempts: {tries}\n')

    guess = 0
    while guess != generated_number:
        guess = int(input('Make a guess: '))
        tries = compare_numbers(guess, generated_number, tries)

        if tries == 0:
            print("You've run out of guesses, you lose.")
            return
            
        elif guess != generated_number:
            print(f"Guess again.\nYou have {tries} attempts remaining to guess the number.\n")
            

play_game()










