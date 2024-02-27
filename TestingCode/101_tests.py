auction_bidders = {'Alex': 1000, 'Jim': 900, 'Kim': 800, 'Joe': 300}

def highest_bidder(auction_bidders):
    max_bid = 0
    winner = ''
    for bidder in auction_bidders:
        current_bid = auction_bidders[bidder]
        if current_bid > max_bid:
            max_bid = current_bid
            winner = bidder
    print(f'Winner is {winner} with {max_bid} EUROS. Congrats!')

highest_bidder(auction_bidders)

    
























