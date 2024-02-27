'''
Rules

    Rock wins against scissors (0 and 2)
    Paper wins against rock (1 and 0)
    Scissors wins against paper (2 and 1)
'''

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
rps = ['rock', 'paper', 'scissors']
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if player_choice < 0 or player_choice > 2:      # or, if player_choice not in [0, 1, 2]:
    print('Values should be 0, 1 or 2. Try again!')
else: 
    print(f'Player chose {rps[player_choice]}')
    print(game_images[player_choice])

    computer_choice = random.randint(0,2)
    print(f'Computer chose {rps[computer_choice]}')
    print(game_images[computer_choice])

    if (player_choice == 0 and computer_choice == 2) or (player_choice == 1 and computer_choice == 0) or (player_choice == 2 and computer_choice == 1):
        print('Player wins')
    elif player_choice == computer_choice:
        print("It's a draw")
    else: 
        print('Computer wins')


    # código simplificado utilizando aritmética modular
    
    aritm_modular = (player_choice - computer_choice) % 3 
    print('Utilizando aritmética modular')
    if aritm_modular == 1:
        print('Player wins')
    elif aritm_modular == 2:
        print('Computer wins')
    else:
        print("It's a draw")






