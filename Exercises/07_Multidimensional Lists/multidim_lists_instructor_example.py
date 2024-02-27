'''
Multidimensional Lists

Instructor's example.
Consider a course where you would like to keep test scores of students. Assuming that each student takes 3 tests.
How do you store student grades?
'''

# Main Program
course = [['Bunny', 90, 87, 95], ['Duck', 78, 96, 89], ['Rob', 83, 85, 92]]

x = course[1]
y = x[2]
z = course[2][0][1]
print(z)
for i, students in enumerate(course):
    print('')
    print('Name: ', students[0])
    total_grade = 0
    count_tests = 0
    for grade_index in range(1, len(students)):
        print(' '*8, students[grade_index])
        total_grade += students[grade_index]
        count_tests += 1
    print('-'*15)
    print('Average:', int(total_grade/count_tests))



