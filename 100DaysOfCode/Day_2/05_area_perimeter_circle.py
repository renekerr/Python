# This program calculates the area and perimeter of a circle

user_response = input("Please input the radius of the circle: ")
radius = int (user_response) # This converts string returns from input() into a number (integer)

area = (radius * radius) * 3.14
perimeter = (radius * 2) * 3.14

print ("The area of the circle is: ", area)
print ("The perimeter of the circle is: ", perimeter)


