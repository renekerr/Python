# ASCII Art : https://ascii.co.uk/art

print('Welcome to Treasure Island.')
print('Your mission is to find the treasure.')

lr_choose = input('You\'re at a cross road.\nDo you want to go "left" or "right"? ')
#using a backslash \ to ignore a symbol
lr_choose = lr_choose.lower()

#Or use lower() function 
#lr_choose = input('You\'re at a cross road.\nDo you want to go "left" or "right"? ').lower()


if lr_choose == 'left':
    #Continue in the game
    ws_choose = input('You\'ve come to a big lake.\nThere is an island in the middle of the lake.\nIn order to get to the island, do you want to "wait" for a boat or "swim" across? ')
    ws_choose = ws_choose.lower()
    if ws_choose == 'wait':
        color_choose = input("You arrive to the island safe.\nThere is a house whit three doors.\nOne 'red', one 'yellow' and one 'blue'.\nTreasure is behind one them.\nWhich one do you choose? ")
        color_choose = color_choose.lower()
        if color_choose == 'yellow':
            print('You have won, treasure is yours!') # Winning choice
        elif color_choose == 'red':
            print('You burned by fire. Game is over!')
        elif color_choose == 'blue':
            print('Eaten by a giant beast. Game is over!')    
        else: 
            print('Door choosen does not exist. Game is over!')
    else: 
        print('You have been attacked by a giant fish. Game is over!')
else:
    print('You just fall on into a hole. Game is over!')
        






