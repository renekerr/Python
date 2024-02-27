#!/usr/bin/env python3.7
# Using Python Dictionaries


# Set the emails variable to be an empty dictionary
emails = {'rene': 'renek@gmail.com', 'julio': 'jcge@gmail.com', 'yudith': 'ylbug@gmail.com'}
print ('Original list: ', list(emails))

# Length of the dictionary
l = len(emails)
print ('Dict length is : ', l)

# Check if key is in dictionary
k = 'rene'
s = k in emails
print ("'" + k + "' is in dictionary :?", s)

# Return an iterator over the keys of the dictionary
i = list(iter(emails))
print (i)

# Add more emails to the dictionary without reassigning the variable.
emails ['alex'] = 'alexk@gmail.com'
print ('Adding item to the list: ', list(emails))

# Remove item from dictionary
del emails ['yudith']
print ('Deleting item from the list: ', list(emails))

# Adding another item
emails ['dalton'] = 'daltonmad@gmail.com'
print ('Adding item to the list: ', list(emails))

# List keys
users = list(emails.keys())
print (users)

# List values
users_emails = list(emails.values())
print (users_emails)


# Return a list of tuples called `pairs` representing the key/value pairs in `emails`
pairs = list(emails.items())
print(pairs)





