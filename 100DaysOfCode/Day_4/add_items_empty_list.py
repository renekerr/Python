# Adding items to an empty list
names = []
end_add = False

while not end_add:
    n = input('Enter your name: ')
    
# Most common ways to add items to an empty list
    names.append(n)
    #names.extend([n])
    #names = names + [n]
    #names.insert(0, n)

    yes_not = input("Someone else to add to the list, type 'yes' or 'no'. ")

    if yes_not == 'no':
        end_add = True
        print(names)
        print('Goodbye')
    else:
        end_add = False