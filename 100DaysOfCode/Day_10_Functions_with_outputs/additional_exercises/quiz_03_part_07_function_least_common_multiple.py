# Quiz 3, Part 7
# Write a function that accepts two positive integers as function parameters and returns their least common multiple (LCM).
# The LCM of two integers a and b is the smallest (non zero) positive integer that is divisible by both a and b.
# For example, the LCM of 4 and 6 is 12, the LCM of 10 and 5 is 10.

def mcm(a,b):

    copy_of_a = a  # make a copy of a

    # While the remainder when a is divided by b is not 0
    # continue to add a to its backup (copy_of_a)

    while copy_of_a%b != 0:
        copy_of_a = copy_of_a + a
    return copy_of_a

m = mcm(2,4)
print(m)
