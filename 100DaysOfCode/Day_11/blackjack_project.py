import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player, computer = [], []
player_score, computer_score = 0, 0


start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if start_game == 'y':

    # First two cards
    for i in range(2):
        player.append(random.choice(cards))
        player_score += player[i]
        computer.append(random.choice(cards))
        computer_score += computer[i]
    
    print(f"Your cards: {player}, current score: {player_score}")
    print(f"Computer's first card: {computer[0]}")
    # print(f"Computer's first card: {computer}, current score: {computer_score}")

    getcard_or_pass = input("Type 'y' to get another card, type 'n' to pass: ")
    if getcard_or_pass == 'y':
        # Get another card
        player.append(random.choice(cards))
        player_score = player_score + player[-1]
        print(f"Your cards: {player}, current score: {player_score}")
        if player_score > 21:
            print(f"Your final hand: {player}, final score: {player_score}")
            print(f"Computer's final hand: {computer}, final score: {computer_score}")
            print('You went over. You lose 😭')
      
elif start_game == 'n':
    print('Goodbye')














# def first_round():
#     player_score, computer_score= 0, 0
    
#     for i in range(2):
#         player_first_two_cards = player.append(random.choice(cards))
#         player_score += player[i]
#         computer_first_two_cards = computer.append(random.choice(cards))
#         computer_score += computer[i]
    
#     return player_first_two_cards, player_score, computer_first_two_cards, computer_score, player, computer