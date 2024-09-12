# Paige Davidson
# CS1400 - MO1
# Assignment 2

# import math modules
import math
from math import pi, tan


# user input
n = eval(input("Enter Number of Sides: "))
s = eval(input("Enter Length of Sides: "))

# calculation
area = round((n * math.pow(s, 2)) / (4 * tan(pi / n)), 5)

# result
print("The Area of the Polygon is: " + str(area))
