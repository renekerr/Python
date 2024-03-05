import random

def deal_cards():
    """
    Return a random card from the deck.
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """
    Return the sum of all cards in a list of cards passed as a parameter
    Check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    Check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)


player_cards, computer_cards = [],[]
game_over = False

start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if start_game == 'y':
    # First two cards
    for _ in range(2):
        player_cards.append(deal_cards())
        computer_cards.append(deal_cards())
    
    #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
    #Hint 9: If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    player_score = calculate_score(player_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Computer's first card: {computer_cards[0]}")
   
    if player_score == 0 or computer_score == 0 or player_score > 21:
        print('Game over.')
        game_over = True
    # If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
    else:
        getcard_or_pass = input("Type 'y' to get another card, type 'n' to pass: ")
        if getcard_or_pass == 'y':
            player_cards.append(deal_cards())
        else:
            print('Game over.')
            game_over = True



else:
    print('Bye')





        









    





