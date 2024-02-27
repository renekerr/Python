"""
List Manipulation Exercise 8 (Adding Odds from 2 Lists)

[This is how multiple line comments are included in Python]

Write a function that accepts two lists both of which consists of
integers and returns the total sum of all the odd integers from both lists.

"""

# Define function
def adding_odds_from_lists(list_a, list_b):

    sum_odds = 0
    list_a.extend(list_b)

    for element in list_a:
        if element % 2 != 0:
            sum_odds = sum_odds + element
    return sum_odds



# Main program
list_a = [23, 1, 2, 5]
list_b = [1, 44, 10, 34, 35]

fn = adding_odds_from_lists(list_a, list_b)

print(fn)





