# Python Loops

up_number = int(input('Values to process: '))

for i in range(1, up_number + 1):
    if i % 3 == 0 and i % 5 == 0:
        print(i, ' is a multiple of 3 and 5')
    elif i % 3 == 0:
        print(i, ' is a multiple of 3')
    elif i % 5 == 0:
        print(i, ' is a multiple of 5')
    else:
        print(i)






