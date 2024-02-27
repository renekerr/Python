'''

#INTRODUCTION TO PYTHON FOR DATA SCIENCE

'''




'''
Python Basics. List, a data structure

-Use the IPython Shell for experimentation, and the script to write successive lines of code.
-Python scripts have the extension .py. my_analysis.py is an example of a script name.
-If you do a calculation in the IPython Shell, the result is immediately printed out. If you do the same thing in the script and run it, this printout will not occur.

In Python 3, you will need print(3 + 4). You need to explicitly include this print() function; otherwise the result will not be printed out when you run the script.

-When to use Python?
You want to do some quick calculations. 
For your new business, you want to develop a database-driven website. 
Your boss asks you to clean and analyze the results of the latest satisfaction survey.

Python Lists
-It is a way to name a collection of values, instead of having to create separate variables for each element. It is a way to name a collection of values, instead of having to create separate variables for each element. - correcto

-The type of a list is simply list.
'''



'''
------------------------------------------------------------------------------------------
INTERACTIVE EXERCISES FOR PYTHON LISTS
LAB EXERCISES
------------------------------------------------------------------------------------------

1-CREATE A LIST

As opposed to int, bool etc, a list is a compound data type: you can group values together:

a = "is"
b = "nice"
my_list = ["my", "list", a, b]

After measuring the height of your family, you decide to collect some information on the house you're living in. The areas of the different parts of your house are stored in separate variables for now, as shown in the script.

INSTRUCTIONS
-Create a list, areas, that contains the area of the hallway (hall), kitchen (kit), living room (liv), bedroom (bed) and bathroom (bath), in this order. Use the predefined variables.
-Print areas with the print() function.
'''

#__________________________________________________________________________________________
script.py
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas = [hall, kit, liv, bed, bath]

# Print areas
print(areas)
#__________________________________________________________________________________________

'''
2-CREATE A LIST WITH DIFFERENT TYPES

A list can contain any Python type. Although it's not really common, a list can also contain a mix of Python types including strings, floats, booleans, etc.

The printout of the previous exercise wasn't really satisfying. It's just a list of numbers representing the areas, but you can't tell which area corresponds to which part of your house.

The code on the right is the start of a solution. For some of the areas, the name of the corresponding room is already placed in front. Pay attention here! "bathroom" is a string, while bath is a variable that represents the float 9.50 you specified earlier.

INSTRUCTIONS
-Finish the line of code that creates the areas list such that the list first contains the name of each room as a string, and then its area. More specifically, add the strings "hallway", "kitchen" and "bedroom" at the appropriate locations.
-Print areas again; is the printout more informative this time?
'''
#__________________________________________________________________________________________
script.py
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = ['hallway',hall, 'kitchen',kit, "living room", liv, 'bedroom',bed, "bathroom", bath]

# Print areas
print(areas)
#__________________________________________________________________________________________

'''
3-LIST OF LISTS

As a data scientist, you'll often be dealing with a lot of data, and it will make sense to group some of this data.

Instead of creating a flat list containing strings and floats, representing the names and areas of the rooms in your house, you can create a list of lists. The script on the right can already give you an idea.

Don't get confused here: "hallway" is a string, while hall is a variable that represents the float 11.25 you specified earlier.

INSTRUCTIONS
-Finish the list of lists so that it also contains the bedroom and bathroom data. Make sure you enter these in order!
-Print out house; does this way of structuring your data make more sense?
-Print out the type of house. Are you still dealing with a list?
'''

#__________________________________________________________________________________________
script.py
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# house information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ['bedroom', bed],
         ['bathroom',bath]]

# Print out house
print(house)

# Print out the type of house
print(type(house))
#__________________________________________________________________________________________




'''
-SUBSETTING LISTS
You use square brackets to subset lists in Python.

You use square brackets for subsetting. Inside the square brackets, simply put the the index of the element you want to access.

List slicing is a very powerful technique to extract several list elements from a list at the same time. In Python, the begin index is included in the slice, the end index is not.

'''

'''
------------------------------------------------------------------------------------------
INTERACTIVE EXERCISES FOR LIST SUBSETTING IN PYTHON
LAB EXERCISES
------------------------------------------------------------------------------------------

1-SUBSET AND CONQUER

Subsetting Python lists is a piece of cake. Take the code sample below, which creates a list x and then selects "b" from it. Remember that this is the second element, so it has index 1. You can also use negative indexing.

x = list["a", "b", "c", "d"]
x[1]
x[-3] # same result!
Remember the areas list from before, containing both strings and floats? Its definition is already in the script. Can you add the correct code to do some Python subsetting?

INSTRUCTIONS
-Print out the second element from the areas list, so 11.25.
-Subset and print out the last element of areas, being 9.50. Using a negative index makes sense here!
-Select the number representing the area of the living room and print it out.
'''

#__________________________________________________________________________________________
script.py
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[1])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[5])
#__________________________________________________________________________________________



'''
2-SUBSET AND CALCULATE

After you've extracted values from a list, you can use them to perform additional calculations. Take this example, where the second and fourth element of a list x are extracted. The strings that result are pasted together using the + operator:

x = ["a", "b", "c", "d"]
print(x[1] + x[3])
INSTRUCTIONS
-Using a combination of list subsetting and variable assignment, create a new variable, eat_sleep_area, that contains the sum of the area of the kitchen and the area of the bedroom.
-Print this new variable eat_sleep_area.
'''

#__________________________________________________________________________________________
script.py
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Sum of kitchen and bedroom area: eat_sleep_area
eat_sleep_area = areas[3] + areas[7]

# Print the variable eat_sleep_area
print(eat_sleep_area)
#__________________________________________________________________________________________


'''
3-SLICING AND DICING

Selecting single values from a list is just one part of the story. It's also possible to slice your list, which means selecting multiple elements from your list. Use the following syntax:

my_list[start:end]
The start index will be included, while the end index is not.

The code sample below shows an example. A list with "b" and "c", corresponding to indexes 1 and 2, are selected from a list x:

x = ["a", "b", "c", "d"]
x[1:3]
The elements with index 1 and 2 are included, while the element with index 3 is not.

INSTRUCTIONS
-Use slicing to create a list, downstairs, that contains the first 6 elements of areas.
-Do a similar thing to create a new variable, upstairs, that contains the last 4 elements of areas.
-Print both downstairs and upstairs using print().
'''

#__________________________________________________________________________________________
script.py
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[0:6]

# Use slicing to create upstairs
upstairs = areas[6:10]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)
#__________________________________________________________________________________________


'''
4-SLICING AND DICING (2)

In the video, Filip only discussed the syntax where you specify both where to begin and end the slice of your list:

my_list[begin:end]
However, it's also possible not to specify these indexes. If you don't specify the begin index, Python figures out that you want to start your slice at the beginning of your list. If you don't specify the end index, the slice will go all the way to the last element of your list. To experiment with this, try the following commands in the IPython Shell:

x = ["a", "b", "c", "d"]
x[:2]
x[2:]
x[:]
INSTRUCTIONS
Use slicing to create the lists downstairs and upstairs again, but this time without using indexes if it's not necessary. Remember downstairs is the first 6 elements of areas and upstairs is the last 4 elements of areas.
'''

#__________________________________________________________________________________________
script.py
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Alternative slicing to create downstairs
downstairs = areas[:6]

# Alternative slicing to create upstairs
upstairs = areas[6:]
#__________________________________________________________________________________________


'''
-MANIPULATING LISTS

Review Questions
You have a list x that is defined as follows:

x = ["a", "b", "b"]

You need to change the second "b" (the third element) to "c".
Which command should you use?

    x[2] = "c"

EXPLANATION
The third element has index 2. You want to change this element with a string, so you need "c" instead of c.

You have a list x that is defined as follows:
x = ["a", "b", "c"]

Which line of Python code do you need to add "d" at the end of the list x?
    
    x = x + ["d"]

EXPLANATION
You basically have to create a single-element list containing "d" and add that to the list x. Next you have to assign the result of this addition to x again to actually update x for the future.
'''

'''
------------------------------------------------------------------------------------------
INTERACTIVE EXERCISES FOR LIST MANIPULATION
LAB EXERCICES
------------------------------------------------------------------------------------------

1-REPLACE LIST ELEMENTS

Replacing list elements is pretty easy. Simply subset the list and assign new values to the subset. You can select single elements or you can change entire list slices at once.

Use the IPython Shell to experiment with the commands below. Can you tell what's happening and why?

x = ["a", "b", "c", "d"]
x[1] = "r"
x[2:] = ["s", "t"]

For this and the following exercises, you'll continue working on the areas list that contains the names and areas of different rooms in a house.

INSTRUCTIONS
-You did a miscalculation when determining the area of the bathroom; it's 10.50 square meters instead of 9.50. Can you make the changes?
-Make the areas list more trendy! Change "living room" to "chill zone".
'''

#__________________________________________________________________________________________
script.py
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[-1] = 10.50

# Change "living room" to "chill zone"
areas[4]='chill zone'
#__________________________________________________________________________________________


'''
2-EXTEND A LIST

If you can change elements in a list, you sure want to be able to add elements to it, right? You can use the + operator:

x = ["a", "b", "c", "d"]
y = x + ["e", "f"]

You just won the lottery, awesome! You decide to build a poolhouse and a garage. Can you add the information to the areas list?

INSTRUCTIONS
-Use the + operator to paste the list ["poolhouse", 24.5] to the end of the areas list. Store the resulting list as areas_1.
-Further extend areas_1 by adding data on your garage. Add the string "garage" and float 15.45. Name the resulting list areas_2.
'''

#__________________________________________________________________________________________
script.py
# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0, 
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ['garage', 15.45]
#__________________________________________________________________________________________


'''
3-DELETE LIST ELEMENTS

Finally, you can also remove elements from your list. You can do this with the del statement:

x = ["a", "b", "c", "d"]
del(x[1])
Pay attention here: as soon as you remove an element from a list, the indexes of the elements that come after the deleted element all change!

The updated and extended version of areas that you've built in the previous exercises is coded below. You can copy and paste this into the IPython Shell to play around with the result.

areas = ["hallway", 11.25, "kitchen", 18.0, 
        "chill zone", 20.0, "bedroom", 10.75, 
         "bathroom", 10.50, "poolhouse", 24.5, 
         "garage", 15.45]
There was a mistake! The amount you won with the lottery is not that big after all and it looks like the poolhouse isn't going to happen. You decide to remove the corresponding string and float from the areas list.

The ; sign is used to place commands on the same line. The following two code chunks are equivalent:

# Same line
command1; command2

# Separate lines
command1
command2

Which of the code chunks will do the job for us?

Possible Answers

del(areas[10]); del(areas[11]) 
del(areas[10:11]) 
del(areas[-4:-2]) correct one!
del(areas[-3]); del(areas[-4])
'''

'''
4-INNER WORKING OF LISTS

At the end of the video, Filip explained how Python lists work behind the scenes. In this exercise you'll get some hands-on experience with this.

The Python code in the script already creates a list with the name areas and a copy named areas_copy. Next, the first element in the areas_copy list is changed and the areas list is printed out. If you hit Submit Answer you'll see that, although you've changed areas_copy, the change also takes effect in the areas list. That's because areas and areas_copy point to the same list.

If you want to prevent changes in areas_copy to also take effect in areas, you'll have to do a more explicit copy of the areas list. You can do this with list() or by using [:].

INSTRUCTIONS
-Change the second command, that creates the variable areas_copy, such that areas_copy is an explicit copy of areas
-Now, changes made to areas_copy shouldn't affect areas. Hit Submit Answer to check this.
'''

#__________________________________________________________________________________________
script.py
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Create areas_copy
areas_copy = areas[:]

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)
#__________________________________________________________________________________________







