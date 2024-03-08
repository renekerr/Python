'''
Write a program that calculates the average student height from a List of heights.
Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.

Example Input 2
151 145 179

Example Output 2
total height = 475
number of students = 3
average height = 158
'''
student_height = [151, 145, 179]
total_height = 0
student_count = 0
average_height = 0
for h in student_height:
  total_height += h
  student_count += 1

average_height = total_height / student_count

print(f'total height = {total_height}')
print(f'number of students = {student_count}')
print(f'average height = {average_height:.0f}')