# Quiz 3, Part 8
# Write a function that accepts two positive integers as parameters. The first integer is the number of heads and the
# second integer is the number of legs of all the creatures in a farm which consists of chickens and dogs.
# Your function should calculate and return the number of chickens and number of dogs in the farm in a list as
# specified below. If it is impossible to determine the correct number of chickens and dogs with the given information
# then your function should return None.

def puzzle(heads,legs):
    dogs = (legs-heads*2)/2

    if dogs<0 or dogs%1:
        return None
    dogs = int(dogs)
    chickens = heads - dogs

    if chickens<0:
        return None
    return [chickens, dogs]

# Main program
p = puzzle(5,12)
print(p)

