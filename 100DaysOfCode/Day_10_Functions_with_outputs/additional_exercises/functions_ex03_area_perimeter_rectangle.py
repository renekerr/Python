# Functions Exercise 3 (Area of Rectangle)
# This program calculates the area and perimeter of a rectangle

def rect_a_p(height_rect,width_rect):
    rect_area = height_rect * width_rect
    rect_perim = 2 * (height_rect + width_rect)
    result = [rect_area,rect_perim] # results as a list
    return result


# Main program
r = rect_a_p(10,30)
print(r)


