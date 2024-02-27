'''
Dictionary Exercise 9 (Day of the Week)

Write a function that accepts a string which contains a particular date from the Gregorian calendar.
Your function should return what day of the week it was. Here are a few examples of what the input
string(Month Day Year) will look like. However, you should not 'hardcode' your program to work only for these input!

"June 12 2012"
"September 3 1955"
"August 4 1843"

Note that each item (Month Day Year) is separated by one space. For example if the input string is:

"May 5 1992"

Then your function should return the day of the week (string) such as:

"Tuesday"

Algorithm with sample example:

# Assume that input was "May 5 1992"
day (d) = 5        # It is the 5th day
month (m) = 3      # (*** Count starts at March i.e March = 1, April = 2, ... January = 11, February = 12)
century (c) = 19   # the first two characters of the century
year (y) = 92      # Year is 1992 (*** if month is January or february decrease one year)
# Formula and calculation
day of the week (w) = (d + floor(2.6m - 0.2) - 2c + y + floor(y/4) + floor(c/4)) modulo 7
after calculation we get, (w) = 2
Count for the day of the week starts at Sunday, i.e Sunday = 0, Monday = 1, Tuesday = 2, ... Saturday = 6

Since we got 2, May 5 1992 was a Tuesday
'''

# Define Function(s)
def day_of_the_week(s):
    output = ''
    s_splitted = s.split()
    print(s_splitted)

    day = s_splitted[1]
    month = s_splitted[0]
    year =s_splitted[2]

    print(day, month, year)

    return s



# Main Program
date_sample = 'May 14 1974'
fn = day_of_the_week(date_sample)

print(fn)