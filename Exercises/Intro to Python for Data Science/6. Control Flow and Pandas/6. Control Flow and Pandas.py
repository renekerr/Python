'''

#INTRODUCTION TO PYTHON FOR DATA SCIENCE






Further readings: 
https://docs.python.org/3.5/tutorial/controlflow.html
https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not
http://pandas.pydata.org
'''

'''
BOOLEAN LOGIC AND CONTROL FLOW

------------------------------------------------------------------------------------------
INTERACTIVE EXERCISES FOR BOOLEAN LOGIC AND CONTROL FLOW
LAB EXERCISES
------------------------------------------------------------------------------------------

1-EQUALITY

To check if two Python values, or variables, are equal, you can use ==. To check for inequality, you need !=. As a refresher, have a look at the following examples, that all result in True. Feel free to try them out in the IPython Shell.

        2 == (1 + 1)
        "intermediate" != "python"
        True != False
        "Python" != "python"

When you write these comparisons in a script, you will need to wrap a print() function around them, to see the output.

INSTRUCTIONS
-In the editor on the right, write code to see if True equals False.
-Write Python code to check if -5 * 15 is not equal to 75.
-Ask Python whether the strings "pyscript" and "PyScript" are equal.
-What happens if you compare booleans and integers? Write code to see if True and 1 are equal.
'''

#__________________________________________________________________________________________
script.py
# Comparison of booleans
print(True == False)

# Comparison of integers
print(-5*15 != 75)

# Comparison of strings
print("pyscript" == "PyScript")

# Compare a boolean with an integer
print(True == 1)
#__________________________________________________________________________________________


'''
2-GREATER AND LESS THAN
In the video, Filip also talked about the less than and greater than signs, < and > in Python. You can combine them with an equals sign: <= and >=. Pay attention: <= is valid syntax, =< is not.

All Python expressions in the following code chunk evaluate to True:

3 < 4
3 <= 4
"alpha" <= "beta"
Remember that for string comparison, Python determines the relationship based on alphabetical order.

INSTRUCTIONS
Write Python expressions, wrapped in a print() function, to check whether:

    -x is greater than or equal to -10. x has already been defined for you.
    -"test" is less than or equal to y. y has already been deinfed for you.
    -True is greater than False.
'''

#__________________________________________________________________________________________
script.py
# Comparison of integers
x = -3 * 6
print(x>=-10)

# Comparison of strings
y = "test"
print('test'<=y)

# Comparison of booleans
print(True>False)
#__________________________________________________________________________________________

'''
3-AND, OR, NOT (1)

A boolean is either 1 or 0, True or False. With boolean operators, such as and, or and not, you can combine these booleans to perform more advanced queries on your data.

In the sample code on the right, two variables are defined: my_kitchen and your_kitchen, representing areas.

INSTRUCTIONS
Write Python expressions, wrapped in a print() function, to check whether:

    -my_kitchen is bigger than 10 and smaller than 18.
    -my_kitchen is smaller than 14 or bigger than 17.
    -double the area of my_kitchen is smaller than triple the area of your_kitchen.    
'''
#__________________________________________________________________________________________
script.py
# Define variables
my_kitchen = 18.0
your_kitchen = 14.0

# my_kitchen bigger than 10 and smaller than 18?
print(my_kitchen>10 and my_kitchen<18)

# my_kitchen smaller than 14 or bigger than 17?
print(my_kitchen<14 or my_kitchen>17)

# Double my_kitchen smaller than triple your_kitchen?
print(my_kitchen*2 < your_kitchen*3)
#__________________________________________________________________________________________


'''
4-AND, OR, NOT (2)

To see if you completely understood the boolean operators, have a look at the following piece of Python code:

    x = 8
    y = 9
    not(not(x < 3) and not(y > 14 or y > 10))

What will the result be if you exectue these three commands in the IPython Shell?

NB: Notice that not has a higher priority than and and or, it is executed first.

Possible Answers
    True
    False CORRECT
    Running these commands will result in an error.


5-WARMUP

To experiment with if and else a bit, have a look at this code sample:

        area = 10.0
        if(area < 9) :
            print("small")
        elif(area < 12) :
            print("medium")
        else :
            print("large")

What will the output be if you run this piece of code in the IPython Shell?

Possible Answers
small
medium CORRECT
large
The syntax is incorrect; this code will produce an error.

6-IF

It's time to take a closer look around in your house.

Two variables are defined in the sample code: room, a string that tells you which room of the house we're looking at, and area, the area of that room.

INSTRUCTIONS
-Examine the if statement that prints out "Looking around in the kitchen." if room equals "kit".
-Write another if statement that prints out "big place!" if area is greater than 15.
'''

#__________________________________________________________________________________________
script.py
# Define variables
room = "kit"
area = 14.0

# if statement for room
if room == "kit" :
    print("looking around in the kitchen.")

# if statement for area
if area > 15:
    print('big place!')
#__________________________________________________________________________________________


'''
7-ADD ELSE

On the right, the if construct for room has been extended with an else statement so that "looking around elsewhere." is printed if the condition room = "kit" evaluates to False.

Can you do a similar thing to add more functionality to the if construct for area?

INSTRUCTIONS
-Add an else statement to the second control structure so that "pretty small." is printed out if area > 15 evaluates to False.
'''

#__________________________________________________________________________________________
script.py
# Define variables
room = "kit"
area = 14.0

# if-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
else :
    print("looking around elsewhere.")

# if-else construct for area
if area > 15 :
    print("big place!")
else:
    print('pretty small.')
#__________________________________________________________________________________________


'''
8-CUSTOMIZE FURTHER: ELIF

It's also possible to have a look around in the bedroom: the sample code contains an elif part that checks if room equals "bed". In that case, "looking around in the bedroom." is printed out.

Up to you now: make a similar addition to the second control structure to further customize the messages for different values of area.

INSTRUCTIONS
-Add an elif to the second control structure such that "medium size, nice!" is printed out if area is greater than 10.
'''

#__________________________________________________________________________________________
script.py
# Define variables
room = "bed"
area = 14.0

# if-elif-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
elif room == "bed":
    print("looking around in the bedroom.")
else :
    print("looking around elsewhere.")

# if-elif-else construct for area
if area > 15 :
    print("big place!")
elif area > 10:
    print("medium size, nice!")
else :
    print("pretty small.")
#__________________________________________________________________________________________


'''
PANDAS

Review Question 1

How is a Pandas DataFrame different from a 2D Numpy array?
    In Pandas, different columns can contain different types. CORRECT

EXPLANATION

Both Pandas and Numpy offer many different ways of subsetting. 
2D Numpy arrays can only contain values of the same basic type, a downside compared to Pandas 
if you're working on typical Data Science problems.

Review Question 2
What are two characteristics that describe Pandas DataFrame?

    The rows correspond to observations. CORRECT
    The rows correspond to variables. 
    The columns correspond to observations 
    The columns correspond to variables. CORRECT

EXPLANATION
Rows correspond to observations; columns correspond to variables, or properties, of these observations.


Review Question 3
Which Pandas function do you use to import data from a comma-separated value (CSV) file into a Pandas DataFrame?

    read_csv() CORRECT

EXPLANATION

read_csv() is the function you need. You can specify a ton of other arguments to customize the way the data is imported. 
To learn about those, have a look at the documentation of read_csv().

Review Question 4
Which technique should you use to select an entire row by its row label when accessing data in a Pandas DataFrame?
    
    loc. CORRECT

EXPLANATION

Square brackets are used to get specific columns from a Pandas DataFrame. 
iloc is used if you want to select a row based on its position in the DataFrame, and not based on its row label.
'''

'''
------------------------------------------------------------------------------------------
INTERACTIVE EXERCISES FOR PANDAS
LAB EXERCISES
------------------------------------------------------------------------------------------

1-CSV TO DATAFRAME (1)

The DataFrame is one of Pandas' most important data structures. It's basically a way to store tabular data, where you can label the rows and the columns.

In the exercises that follow, you will be working wit vehicle data in different countries. Each observation corresponds to a country, and the columns give information about the number of vehicles per capita, whether people drive left or right, and so on. This data is available in a CSV file, named cars.csv. It is available in your current working directory, so the path to the file is simply 'cars.csv'.

To import CSV data into Python as a Pandas DataFrame, you can use read_csv().

INSTRUCTIONS
-To import CSV files, you still need the pandas package: import it as pd.
-Use pd.read_csv() to import cars.csv data as a DataFrame. Store this dataframe as cars.
-Print out cars. Does everything look OK?
'''

#__________________________________________________________________________________________
script.py
# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv('cars.csv')

# Print out cars
print(cars)
#__________________________________________________________________________________________

'''
2-CSV TO DATAFRAME (2)

Your read_csv() call to import the CSV data didn't generate an error, but the output is not entirely what you'd want: the row labels are imported as another column, that has no name.

Remember index_col, an argument of read_csv() that you can use to specify which column in the CSV file should be used as a row label? Well, that's exactly what you need here!

Python code that solves the previous exercise is already included; can you make the appropriate changes to fix the data import?

INSTRUCTIONS
-Run the code with Submit Answer and assert that the first column should actually be used as row labels.
-Specify the index_col argument inside pd.read_csv(): set it to 0, so that the first column is used as row labels.
-Has the printout of cars improved now?
'''
#__________________________________________________________________________________________
script.py
# Import pandas as pd
import pandas as pd

# Fix import by including index_col
cars = pd.read_csv('cars.csv',index_col = 0)

# Print out cars
print(cars)
#__________________________________________________________________________________________


'''
3-SQUARE BRACKETS

In the video, you saw that you can index and select Pandas DataFrames in many different ways. The simplest, but the not the most powerful way, is to use square brackets.

In the sample code on the right, the same cars data is imported from a CSV files as a Pandas DataFrame. To select only the cars_per_cap column from cars, you can use:

cars['cars_per_cap']
cars[['cars_per_cap']] 
The single bracket version gives a Pandas Series, the double bracket version gives a Pandas DataFrame.

INSTRUCTIONS
-Use single square brackets to print out the country column of cars as a Pandas Series.
-Use double square brackets to print out the country column of cars as a Pandas DataFrame. 
 Do this by putting country in two square brackets this time.
'''
#__________________________________________________________________________________________
script.py
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out country column as Pandas Series
print(cars['country'])

# Print out country column as Pandas DataFrame
print(cars[['country']])
#__________________________________________________________________________________________


'''
4-LOC (1)

With loc you can do practically any data selection operation on DataFrames you can think of. loc is label-based, which means that you have to specify rows and columns based on their row and column labels.

Try out the following commands in the IPython Shell to experiment with loc to select observations:

    cars.loc['RU']
    cars.loc[['RU']]
    cars.loc[['RU', 'AUS']]

As before, code is included that imports the cars data as a Pandas DataFrame.

INSTRUCTIONS
-Use loc to select the observation corresponding to Japan as a Series. The label of this row is JAP. Make sure to print the resulting Series.
-Use loc to select the observations for Australia and Egypt as a DataFrame. You can find out about the labels of these rows by inspecting cars in the IPython Shell. Make sure to print the resulting DataFrame.
'''
#__________________________________________________________________________________________
script.py
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out observation for Japan
print(cars.loc['JAP'])

# Print out observations for Australia and Egypt
print(cars.loc[['AUS', 'EG']])
#__________________________________________________________________________________________

'''
5-LOC (2)

loc also allows you to select both rows and columns from a DataFrame. To experiment, try out the following commands in the IPython Shell.

    cars.loc['IN', 'cars_per_cap']
    cars.loc[['IN', 'RU'], 'cars_per_cap']
    cars.loc[['IN', 'RU'], ['cars_per_cap', 'country']]

INSTRUCTIONS
-Print out the drives_right value of the row corresponding to Morocco (its row label is MOR)
-Print out a sub-DataFrame, containing the observations for Russia and Morocco and the columns country and drives_right.
'''
#__________________________________________________________________________________________
script.py
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right value of Morocco
print(cars.loc[['MOR'], 'drives_right'])

# Print sub-DataFrame
print(cars.loc[['RU','MOR'],['country','drives_right']])
#__________________________________________________________________________________________

































