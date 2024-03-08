#!/usr/bin/env python3.7
# Using Python Lists


# 1) Set the users variable to be an empty list
users = ['Alex', 'Ana', 'Pedro']

# Add items to list
print('Initial list', users)

# Delete items from list
del users[1]
print('Deleted item', users)

# Adding again
users.append('Ana')
print('Appending item again', users)

# Reversed list
rev_list = list(reversed(users))
print('Reversed list', rev_list)

# Insert user
users.insert(1, 'René')
print('Adding item in specific position', users)

# Adding more items at the end of list
users += ['Juan', 'Pablo', 'José']
print('Adding more items', users)


# Slice the users lists to return the 3rd and 4th items and assign the result to `center_users`
center_users = users[2:5]
print('Center users', center_users)



















