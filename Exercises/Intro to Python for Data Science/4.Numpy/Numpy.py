'''

#INTRODUCTION TO PYTHON FOR DATA SCIENCE






Further readings: 
http://www.numpy.org
'''

'''
NUMPY

Review Questions

-Which Numpy function do you use to create an array?
    
    array()

EXPLANATION
To create a Numpy array, you use the array() function. You typically pass a regular Python list as an input.

-Which two statements describe the advantage of Numpy Package over regular Python Lists?

    The Numpy Package provides the array, a data type that can be used to do element-wise calculations.
    
    Because Numpy arrays can only hold element of a single type, calculations on Numpy arrays 
    can be carried out way faster than regular Python lists.

EXPLANATION
Creating a Numpy array is not necessarily easier, but it is a great solution 
if you want to carry out element-wise calculations, something that regular Python lists aren't capable of.



-What is the resulting Numpy array z after executing the following lines of code?

    import numpy as np
    x = np.array([1, 2, 3])
    y = np.array([3, 2, 1])
    z = x + y

    array([4, 4, 4]) (correct answer)


-What happens when you put an integer, a Boolean, and a string in the same Numpy array using the array() function?

    All array elements are converted to strings. All array elements are converted to strings. - correcto

EXPLANATION
Numpy arrays can only hold elements with the same basic type. 
The string is the most 'general' and free form to store data, so all other data types are converted to strings.
'''

'''
------------------------------------------------------------------------------------------
INTERACTIVE EXERCISES FOR NUMPY
LAB EXERCISES
------------------------------------------------------------------------------------------
1-YOUR FIRST NUMPY ARRAY

We're going to dive into the world of baseball. Along the way, you'll get comfortable with the basics of Numpy, a powerful package to do data science.

A list baseball has already been defined in the Python script, representing the height of some baseball players in centimeters. Can you add some code here and there to create a Numpy array from it?

INSTRUCTIONS
-Import the numpy package as np, so that you can refer to numpy with np.
-Use np.array() to create a Numpy array from baseball. Name this array np_baseball.
-Print out the type of np_baseball to check that you got it right.
'''

#__________________________________________________________________________________________
script.py
# Create list baseball 
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Import the numpy package as np
import numpy as np

# Create a Numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))
#__________________________________________________________________________________________


'''
2-BASEBALL PLAYER'S HEIGHT

You are a huge baseball fan. You decide to call the MLB (Major League Baseball) and ask around for some more statistics on the height of the main players. They pass along data on more than a thousand players, which is stored as a regular Python list: height. The height is expressed in inches. Can you make a Numpy array out of it and convert the units to centimeters?

height is already available and the numpy package is loaded, so you can start straight away (Source: stat.ucla.edu).

INSTRUCTIONS
-Create a Numpy array from height. Name this new array np_height.
-Print np_height.
-Multiply np_height with 0.0254 to convert all height measurements from inches to meters. Store the new values in a new array, np_height_m.
-Print out np_height_m and check if the output makes sense.
'''

#__________________________________________________________________________________________
script.py
# height is available as a regular list

# Import numpy
import numpy as np

# Create a Numpy array from height: np_height
np_height = np.array(height)

# Print out np_height
print(np_height)

# Convert np_height to m: np_height_m
np_height_m = np_height * 0.0254

# Print np_height_m
print(np_height_m)
#__________________________________________________________________________________________


'''
3-BASEBALL PLAYER'S BMI

The MLB also offers to let you analyze their weight data. Again, both are available as regular Python lists: height and weight. height is in inches and weight is in pounds.

It's now possible to calculate the BMI of each baseball player. Python code to convert height to a Numpy array with the correct units is already available in the workspace. Follow the instructions step by step and finish the game!

INSTRUCTIONS
-Create a Numpy array from the weight list with the correct units. Multiply by 0.453592 to go from pounds to kilograms. Store the resulting Numpy array as np_weight_kg.
-Use np_height_m and np_weight_kg to calculate the BMI of each player. Use the following equation:
    
        BMI=weight(kg)height(m)2 (m to the power of 2)

-Save the resulting numpy array as bmi.
Print out bmi.
'''

#__________________________________________________________________________________________
script.py
# height and weight are available as a regular lists

# Import numpy
import numpy as np

# Create array from height with correct units: np_height_m
np_height_m = np.array(height) * 0.0254

# Create array from weight with correct units: np_weight_kg 
np_weight_kg = np.array(weight) * 0.453592

# Calculate the BMI: bmi
bmi = np_weight_kg/np_height_m ** 2


# Print out bmi
print(bmi)
#__________________________________________________________________________________________

'''
4-LIGHTWEIGHT BASEBALL PLAYERS

To subset both regular Python lists and Numpy arrays, you can use square brackets:

    x = [4 , 9 , 6, 3, 1]
    x[1]
    import numpy as np
    y = np.array(x)
    y[1]

For Numpy specifically, you can also use boolean Numpy arrays:

    high = y > 5
    y[high]

The code that calculates the BMI of all baseball players is already included. Follow the instructions and reveal interesting things from the data!

INSTRUCTIONS
-Create a boolean Numpy array: the element of the array should be True if the corresponding baseball player's BMI is below 21. You can use the < operator for this. Name the array light.
-Print the array light.
-Print out a Numpy array with the BMIs of all baseball players whose BMI is below 21. Use light inside square brackets to do a selection on the bmi array.
'''

#__________________________________________________________________________________________
script.py
# height and weight are available as a regular lists

# Import numpy
import numpy as np

# Calculate the BMI: bmi
np_height_m = np.array(height) * 0.0254
np_weight_kg = np.array(weight) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

# Create the light array
light = bmi < 21

# Print out light
print(light)


# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light])
#__________________________________________________________________________________________


'''
5-NUMOPY SIDE EFFECTS

As Filip explained before, Numpy is great to do vector arithmetic. If you compare its functionality with regular Python lists, however, some things have changed.

First of all, Numpy arrays cannot contain elements with different types. If you try to build such a list, some of the elments' types are changed to end up with a homogenous list. This is known as type coercion.

Second, the typical arithmetic operators, such as +, -, * and / have a different meaning for regular Python lists and Numpy arrays.

Have a look at this line of code:

np.array([True, 1, 2]) + np.array([3, 4, False])
Can you tell which code chunk builds the exact same Python data structure? The Numpy package is already imported as np, so you can start experimenting in the IPython Shell straight away!

Possible Answers
np.array([True, 1, 2, 3, 4, False]) 
np.array([4, 3, 0]) + np.array([0, 2, 2])  CORRECT 
np.array([1, 1, 2]) + np.array([3, 4, -1]) 
np.array([0, 1, 2, 3, 4, 5])
'''

'''
6-SUBSETTING NUMPY ARRAYS

You've seen it with your own eyes: Python lists and Numpy arrays sometimes behave differently. Luckily, there are still certainties in this world. For example, subsetting (using the square bracket notation on lists or arrays) works exactly the same. To see this for yourself, try the following lines of code in the IPython Shell:

x = ["a", "b", "c"]
x[1]

np_x = np.array(x)
np_x[1]
The script on the right already contains code that imports numpy as np, and stores both the height and weight of the MLB players as Numpy arrays.

INSTRUCTIONS
-Subset np_weight: print out the element at index 50.
-Print out a sub-array of np_height: It contains the elements at index 100 up to and including index 110
'''

#__________________________________________________________________________________________
script.py
# height and weight are available as a regular lists

# Import numpy
import numpy as np

# Store weight and height lists as numpy arrays
np_weight = np.array(weight)
np_height = np.array(height)

# Print out the weight at index 50
print(np_weight[50])

# Print out sub-array of np_height: index 100 up to and including index 110
print(np_height[100:111])
#__________________________________________________________________________________________


'''
2D NUMPY ARRAYS
Review Question 1

What charaterizes multi-dimensional Numpy arrays?

    You can create a 2D Numpy array from a regular list of lists. - correcto

EXPLANATION

Multi-dimensional Numpy arrays are natural extensions of the 1D Numpy array: 
    They can only hold a single type and can be created from a regular Python list structure. 
    The number N in these N-dimensional Numpy arrays is not limited.


Review Question 2
You created the following 2D Numpy array, x
    import numpy as np
    x = np.array([["a", "b", "c", "d"],
                  ["e", "f", "g", "h"]])

Which Python command do you use to select the string "g" from x?
    x[1,2] - correcto

EXPLANATION

Apart from element-wise calculations, 2D Numpy arrays also offer more advanced ways of subsetting 
compared to regular Python lists of lists. To select the second row, use the index 1 before the comma. 
To select the third column, use the index 2 after the comma.

Review Question 3
What does the resulting array z contain after executing the following lines of Python code?

    import numpy as np
    x = np.array([[1, 2, 3],
                  [1, 2, 3]])
    y = np.array([[1, 1, 1],
                  [1, 2, 3]])
    z = x - y

array([[0, 1, 2],
       [0, 0, 0]]) correcto

'''
'''
------------------------------------------------------------------------------------------
INTERACTIVE EXERCISES FOR 2D NUMPY ARRAYS
LAB EXERCISES
------------------------------------------------------------------------------------------

1-YOUR FIRST 2D NUMPY ARRAY
Before working on the actual MLB data, let's try to create a 2D Numpy array from a small list of lists.

In this exercise, baseball is a list of lists. The main list contains 4 elements. Each of these elements is a list containing the height and the weight of 4 baseball players, in this order. baseball is already coded for you in the script.

INSTRUCTIONS
-Use np.array() to create a 2D Numpy array from baseball. Name it np_baseball.
-Print out the type of np_baseball.
-Print out the shape attribute of np_baseball. Use np_baseball.shape.
'''

#__________________________________________________________________________________________
script.py
# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Import numpy
import numpy as np

# Create a 2D Numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)
#__________________________________________________________________________________________


'''
2-BASEBALL DATA IN 2D FORM

You have another look at the MLB data and realize that it makes more sense to restructure all this information in a 2D Numpy array. This array should have 1015 rows, corresponding to the 1015 baseball players you have information on, and 2 columns (for height and weight).

The MLB was, again, very helpful and passed you the data in a different structure, a Python list of lists. In this list of lists, each sublist represents the height and weight of a single baseball player. The name of this embedded list is baseball.

Can you store the data as a 2D array to unlock Numpy's extra functionality?

INSTRUCTIONS
-Use np.array() to create a 2D Numpy array from baseball. Name it np_baseball.
-Print out the shape attribute of np_baseball.
'''

#__________________________________________________________________________________________
script.py
# baseball is available as a regular list of lists

# Import numpy package
import numpy as np

# Create a 2D Numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the shape of np_baseball
print(np_baseball.shape)
#__________________________________________________________________________________________

'''
3-SUBSETTING 2D NUMPY ARRAYS

If your 2D Numpy array has a regular structure, i.e. each row and column has a fixed number of values, complicated ways of subsetting become very easy. Have a look at the code below where the elements "a" and "c" are extracted from a list of lists.

        # regular list of lists
        x = [["a", "b"], ["c", "d"]]
        [x[0][0], x[1][0]]
        
        # numpy
        import numpy as np
        np_x = np.array(x)
        np_x[:,0]

For regular Python lists, this is a real pain. For 2D Numpy arrays, however, it's pretty intuitive! The indexes before the comma refer to the rows, while those after the comma refer to the columns. The : is for slicing; in this example, it tells Python to include all rows.

The code that converts the pre-loaded baseball list to a 2D Numpy array is already in the script. Add some lines to make the correct selections. Remember that in Python, the first element is at index 0!

INSTRUCTIONS
-Print out the 50th row of np_baseball.
-Make a new variable, np_weight, containing the entire second column of np_baseball.
-Select the height (first column) of the 124th baseball player in np_baseball and print it out.
'''


#__________________________________________________________________________________________
script.py
# baseball is available as a regular list of lists

# Import numpy package
import numpy as np

# Create np_baseball (2 cols)
np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball
print(np_baseball[49,:])

# Select the entire second column of np_baseball: np_weight
np_weight = np_baseball[:,1]

# Print out height of 124th player
print(np_baseball[123,0])
#__________________________________________________________________________________________


'''
4-2D ARITHMETIC

Remember how you calculated the Body Mass Index for all baseball players? Numpy was able to perform all calculations element-wise. For 2D Numpy arrays this isn't any different! You can combine matrices with single numbers, with vectors, and with other matrices.

Execute the code below in the IPython shell and see if you understand:

        import numpy as np
        np_mat = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
        np_mat * 2
        np_mat + np.array([10, 10])
        np_mat + np_mat
        np_baseball is coded for you; it's again a 2D Numpy array with 3 columns representing height, weight and age.

INSTRUCTIONS
-You managed to get hold on the changes in weight, height and age of all baseball players. It is available as a 2D Numpy array, update. Add np_baseball and update and print out the result.
-You want to convert the units of height and weight. As a first step, create a Numpy array with three values: 0.0254, 0.453592 and 1. Name this array conversion.
-Multiply np_baseball with conversion and print out the result.
'''

#__________________________________________________________________________________________
script.py
# baseball is available as a regular list of lists
# update is available as 2D Numpy array

# Import numpy package
import numpy as np

# Create np_baseball (3 cols)
np_baseball = np.array(baseball)

# Print out addition of np_baseball and update
print(np_baseball + update)

# Create Numpy array: conversion
conversion = ([0.0254, 0.453592, 1])

# Print out product of np_baseball and conversion
print(np_baseball * conversion)
#__________________________________________________________________________________________



'''
BASIC STATISTICS WITH NUMPY

Review Question 1
Which of the following statement about basic statistics with Numpy is correct?

Note: assume that the Numpy package is imported as np.

        Numpy offers many functions to calculate basic statistics, such as np.mean(), np.median() and np.std(). CORRECT

EXPLANATION

Both the mean and median are interesting statistics to check out before you start your analysis. 
Visual inspection of your data is practically infeasible if you're dealing with millions of data points.


Review Question 2

You are writing code to measure your travel time and weather conditions to work each day.

The data is recorded in a Numpy array where each row specifies the measurements for a single day.

The first column specifies the temperature in Fahrenheit. The second column specifies the amount of travel time in minutes.

The following is a sample of the code.


import numpy as np
x = np.array([[28, 18],
              [34, 14],
              [32, 16],
              ...
              [26, 23],
              [23, 17]])

Which Python command do you use to calculate the average travel time?

        np.mean(x[:,1]) CORRECT


EXPLANATION

:,1 inside square brackets tells Python to get all the rows, and the second column. 
You can then use np.mean() to get the average of the resulting Numpy array.


Review Question 3

(1/1 punto)
As a wrap up, have a look at the statements below about Numpy in general. Select the three statements that hold.

Numpy is a great alternative to the regular Python list if you want to do Data Science in Python. CORRECT
Numpy arrays can only hold elements of the same basic type. CORRECT

It is not possible perform element-wise calculations with 3D Numpy arrays. INCORRECT

Next to an efficient data structure, Numpy also offers tools to calculate summary statistics and to simulate statistical distributions. CORRECT

EXPLANATION

No matter the dimension of the Numpy array, element-wise calculations will always be possible.
'''

'''
------------------------------------------------------------------------------------------
INTERACTIVE EXERCISES FOR BASIC STATISTICS WITH NUMPY
LAB EXERCISES
------------------------------------------------------------------------------------------

1-AVERAGE VERSUS MEDIAN

You now know how to use Numpy functions to a get a better feeling for your data. It basically comes down to importing Numpy and then calling several simple functions on the Numpy arrays:

        import numpy as np
        x = [1, 4, 8, 10, 12]
        np.mean(x)
        np.median(x)
        The baseball data is available as a 2D Numpy array with 3 columns (height, weight, age) and 1015 rows. The name of this Numpy array is np_baseball. After restructuring the data, however, you notice that some height values are abnormally high. Follow the instructions and discover which summary statistic is best suited if you're dealing with so-called outliers.
    
INSTRUCTIONS
-Create Numpy array np_height, that is equal to first column of np_baseball.
-Print out the mean of np_height.
-Print out the median of np_height.
'''

#__________________________________________________________________________________________
script.py
# np_baseball is available

# Import numpy
import numpy as np

# Create np_height from np_baseball
np_height = np_baseball[:,0]

# Print out the mean of np_height
print(np.mean(np_height))

# Print out the median of np_height
print(np.median(np_height))
#__________________________________________________________________________________________


'''
2-EXPLORE THE BASEBALL DATA

Because the mean and median are so far apart, you decide to complain to the MLB. 
They find the error and send the corrected data over to you. It's again available as a 2D Numpy array np_baseball, with three columns.

The Python script on the right already includes code to print out informative messages with the different summary statistics. 
Can you finish the job?

INSTRUCTIONS
-The code to print out the mean height is already included. Complete the code for the median height. Replace None with the correct code.
-Use np.std() on the first column of np_baseball to calculate stddev. Replace None with the correct code.
-Do big players tend to be heavier? Use np.corrcoef() to store the correlation between the first and second column of np_baseball in corr. Replace None with the correct code.
'''


#__________________________________________________________________________________________
script.py
# np_baseball is available

# Import numpy
import numpy as np

# Print mean height (first column)
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height. Replace 'None'
med = np.median(np_baseball[:,0])
print("Median: " + str(med))

# Print out the standard deviation on height. Replace 'None'
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column. Replace 'None'
corr = np.corrcoef(np_baseball[:,0], np_baseball[:,1])
print("Correlation: " + str(corr))
#__________________________________________________________________________________________


'''
3-BLEND IT ALL TOGETHER

In the last few exercises you've learned everything there is to know about heights and weights of baseball players. Now it's time to dive into another sport: soccer.

You've contacted the FIFA for some data and they handed you two lists. The lists are the following:

        positions = ['GK', 'M', 'A', 'D', ...]
        heights = [191, 184, 185, 180, ...]

Each element in the lists corresponds to a player. The first list, positions, contains strings representing each player's position. The possible positions are: 'GK' (goalkeeper), 'M' (midfield), 'A' (attack) and 'D' (defense). The second list, heights, contains integers representing the height of the player in cm. The first player in the lists is a goalkeeper and is pretty tall (191 cm).

You're fairly confident that the median height of goalkeepers is higher than that of other players on the soccer field. Some of your friends don't believe you, so you are determined to show them using the data you received from FIFA and your newly acquired Python skills.

INSTRUCTIONS
-Convert heights and positions, which are regular lists, to numpy arrays. Call them np_heights and np_positions.
-Extract all the heights of the goalkeepers. You can use a little trick here: use np_positions == 'GK' as an index for np_heights. Assign the result to gk_heights.
-Extract all the heights of the all the other players. This time use np_positions != 'GK' as an index for np_heights. Assign the result to other_heights.
-Print out the median height of the goalkeepers using np.median(). Replace None with the correct code.
-Do the same for the other players. Print out their median height. Replace None with the correct code.
'''

#__________________________________________________________________________________________
script.py
# heights and positions are available as lists

# Import numpy
import numpy as np

# Convert positions and heights to numpy arrays: np_positions, np_heights
np_positions = np.array(positions)
np_heights = np.array(heights)

# Heights of the goalkeepers: gk_heights
gk_heights = np_heights[np_positions == 'GK']


# Heights of the other players: other_heights
other_heights = np_heights[np_positions != 'GK']

# Print out the median height of goalkeepers. Replace 'None'
print("Median height of goalkeepers: " + str(np.median(gk_heights)))

# Print out the median height of other players. Replace 'None'
print("Median height of other players: " + str(np.median(other_heights)))

#__________________________________________________________________________________________






























