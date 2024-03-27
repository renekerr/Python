
# Python Object-Oriented Programming: Circle class with area and perimeter calculation
# Create a class representing a Circle. Include methods to calculate its area and perimeter.

from math import pi

class Circle:

    def __init__(self, r):
        self.radius = r

    def circle_area(self):
        return (self.radius**2) * pi


    def circle_perimeter(self):
        return (self.radius * 2) * pi


radius = float(input('Enter the radius of the circle: '))
circle = Circle(radius)

r = circle.radius
area = circle.circle_area()
perimeter = circle.circle_perimeter()

print(f"Radius : {r}")
print (f"The area of the circle is: {area:.2F}")
print (f"The perimeter of the circle is: {perimeter:.2F}")
