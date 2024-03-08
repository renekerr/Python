'''
Day 5 - loops
'''

'''

LOOPS
                    
'''

# for loop
'''
for item in list_of_items: 
    # Do something to each item
'''

fruit_list = ['Apple', 'Pear', 'Orange']
for fruit in fruit_list:
    print(fruit + ' pie')


# for range loop
'''
for number in range(a, b, step): {b not included}
    print(number)
'''

# Add up all numbers between 1 and 100
total = 0
for n in range(1,101):
    total += n

print(total)

