from random import randint

EASY_LEVEL_TRIES = 10
HARD_LEVEL_TRIES = 5

def validate_guess(guess, generated_number, tries):
    if guess > generated_number: 
        print('Too high.')
        return tries - 1
    elif guess < generated_number:
        print('Too low.')
        return tries - 1
    else:
        print(f'You got it! The answer was {generated_number}')

def difficulty_level():
    level_chosen = input("Choose a difficulty. Type 'easy' or 'hard': ")
    
    print('¨' * 30)
    print(f'Difficulty level: {level_chosen.upper()}')
    
    if level_chosen == 'hard':
        return HARD_LEVEL_TRIES
    elif level_chosen == 'easy':
        return EASY_LEVEL_TRIES

def play_game(): 
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")           
    generated_number = randint(1,100)
    # print(f'Pssst, the correct answer is {generated_number}')

    turns = difficulty_level()
    print(f'Total attempts : {turns}\n')
    
    guess = 0
    while guess != generated_number:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        turns = validate_guess(guess, generated_number, turns)

        if turns == 0:            
            print("You've run out of guesses, you lose.")
            return 
        elif guess != generated_number: 
            print(f"Guess again.")
            
play_game()

