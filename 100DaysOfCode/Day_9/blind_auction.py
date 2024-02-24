'''
The objective is to write a program that will collect the names and bids of different people. The program should ask for each bidder's name and their bid individually.
'''
from art import logo
from mod_clear_screen import clear_screen

print(logo)
end_of_bids = False
auction_bidders = {}

def blind_auction (name, bid):
    auction_bidders[name] = bid
    
    print(auction_bidders)


print('Welcome to the secret auction program')

while not end_of_bids:
    name = input('What is your name? ')
    bid_amount = int(input('What is your bid? '))

    blind_auction(name, bid_amount)

    yes_or_not = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if yes_or_not == 'no':
        end_of_bids = True
        print('Goodbye')
    elif yes_or_not == 'yes':
        end_of_bids = False
        clear_screen()
