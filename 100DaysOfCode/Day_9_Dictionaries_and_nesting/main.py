'''
Day 9 - Dictionaries, Nesting and the Secret Auction
'''

'''
DICTIONARIES & NESTING                                                 

'''


''' DICTIONARIES
Unordered collection of key-value pairs
Accessed by unique keys
Don't allow duplicate keys (keys must be unique)
Keys must be immutable, values can be any data type

Example: 
    Phonebook where you look up contacts by name (key)
'''
# Empty dictionary
programming_dictionary = {}

'''
key : value
'''

# Example of a dictionary
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "A control structure that allows you to execute a block of code repeatedly until a specific condition is met"
}

# Retrive information from a dictionary
print(programming_dictionary["Loop"])

# Adding items to a dictionary
programming_dictionary["Author"] = "Rene Kerr"


# Wipe a dictionary
#programming_dictionary = {}

print(programming_dictionary)


# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."

# loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


for i, elem in enumerate(programming_dictionary):
    print(i, elem, ':', programming_dictionary[elem])


