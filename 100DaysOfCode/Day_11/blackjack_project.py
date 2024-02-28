import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player = []
computer = []

def first_round():
    player_score, computer_score= 0, 0
    
    for i in range(2):
        player_first_two_cards = player.append(random.choice(cards))
        player_score += player[i]
        computer_first_two_cards = computer.append(random.choice(cards))
        computer_score += computer[i]
    
    return player_first_two_cards, player_score, computer_first_two_cards, computer_score, player, computer

start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if start_game == 'y':
    
    first_round()

    print(f"Your cards: {player},  current score: ")
    print(f"Computer's first card: {computer[0]}")
    hit_or_pass = input("Type 'y' to get another card, type 'n' to pass: ")



elif start_game == 'n':
    print('Goodbye')

