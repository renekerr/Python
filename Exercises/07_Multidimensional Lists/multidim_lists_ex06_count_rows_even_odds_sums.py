'''
Multidimensional Lists Exercise 6 (Count Rows with Even and Odd Sums)

Write a function that will receive a 2D list of integers. The function should return the count of how many rows of the
list have even sums and the count of how many rows have odd sums.

For example if the even count was 2, and odd count
was 4 your function should return them in a list like this: [2, 4].
'''

# Define Function(s)
def count_rows_even_odd_sums(list_sample):
    count_even = 0
    count_odd = 0
    for k, elements in enumerate(list_sample):
        s = sum(elements)
        if s % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    return [count_even, count_odd]

# Main Program
input_list = [[1, 2, 3], [10, 10, 20], [4, 1, 6]]
fn = count_rows_even_odd_sums(input_list)

print(fn)

'''
################### Sample Solution ###################
def _count_even_sum_sample_(sample_2d_list):
    even_count = 0
    odd_count = 0
    # For each row
    for rows in sample_2d_list:
        row_sum = sum(rows)
        if row_sum % 2 == 0:
            even_count = even_count + 1
        else:
            odd_count = odd_count + 1
    return [even_count, odd_count]
'''
