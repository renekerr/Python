#!/usr/bin/env python3.7
# Using Python String Methods

# message_text = input('Enter a message: ')
message_text = 'ThIs iS jUst soMe rAndoM texT'
print(message_text)

# Message lowercase
print('lower() method: ', message_text.lower())

# Message uppercase
print('upper() method : ', message_text.upper())

# Message title
print('title() method: ', message_text.title())

# Message capital
print('capitalize() method : ', message_text.capitalize())

# Separate the String and Present the Individual Words as a List
words = message_text.split()
print('Words : ', words)

# Sort words
sorting = sorted(words)

print("Alphabetic First Word:", sorting[0])
print("Alphabetic Last Word:", sorting[-1])









