'''
Write the necessary code calculate the volume and surface area
of a cylinder with a radius of 3.14 and a height of 5. Print out the result.


'''

# Importing the mat module
import math
radius = 3.14
height = 5

area = math.pi * (radius**2) *height
surface_area = 2 * (math.pi * radius**2) + 2 * math.pi * radius * height
print(area, surface_area)
