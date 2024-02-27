'''
Dictionary Exercise 3 (Lists as Values)

Write a function that accepts a dictionary as input which contains the names and grades of students
(The keys are student names and the values are lists of grades for 3 exams (1 Dimensional list)) and returns
the list of names for those students whose grade on all three exams is greater than or equal to 78.
'''

# Define Function(s)
def dict_list_as_values(dict_sample):
    output_list = []                            # Create an empty list to display results
    keys = dict_sample.keys()                   # Get keys from dictionary

    for k in keys:                              # Loop through keys (students names')
        grades_list = dict_sample[k]           # Assign values (dict_sample[k]) to a var named grades_list
        print(k, grades_list)
        grade_1, grade_2, grade_3 = grades_list[0], grades_list[1], grades_list[2]

        if grade_1 >= 78 and grade_2 >= 78 and grade_3 >= 78:

            # Check condition, if True key (student's name) will be appended to list
            output_list.append(k)

    return output_list                                     # Return list with results

# Main Program
d = {'Alex':[100, 100, 79], 'Luis':[60, 65, 70], 'Alberto':[100, 100, 90]}
fn = dict_list_as_values(d)
print(fn)


'''
################### Sample Solution ###################
def _dictionary_names_grades_sample_(sample_dictionary):
    output_list = []
    keys = sample_dictionary.keys()
    for k in keys:
        each_list = sample_dictionary[k]
        grade1, grade2, grade3 = each_list[0], each_list[1], each_list[2]
        if grade1 >= 78 and grade2 >= 78 and grade3 >= 78:
            output_list.append(k)
    return output_list
'''