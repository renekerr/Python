"""
Midterm Exam, Part 7 (Pattern Sum)

Write a function called pattern_sum that receives two single digit positive integers,
(k and m) as parameters and calculates and returns the total sum as:
k + kk + kkk + .... (the last number in the sequence should have m digits)
For example, if the two integers are:

(4, 5)
Your function should return the total sum of:
4 + 44 + 444 + 4444 + 44444
Notice the last number in this sequence has 5 digits. The return value should be:
49380
if the two integers are:
(5, 3)
Your function should return the total sum of:
5 + 55 + 555
Notice the last number in this sequence has 3 digits. The return value should be:
615
"""

# Define function
def pattern_sum(a,b):
    str_convert = ''
    s = 0

    for i in range(1, b + 1):
        str_convert = str_convert + str(a)
        s = s + int(str_convert)
    return s

# Main program
k = 4
m = 5
my_function = pattern_sum(k,m)

print(my_function)


"""
################### Instructor function ###################
def _chain_of_number_sample_ed2_(a, b):
    chain_list = []
    my_sum = 0
    for x in range(1, b+1):
        chain_list.append(x*str(a))
    for items in chain_list:
        my_sum = my_sum + int(items)

    return my_sum
"""








