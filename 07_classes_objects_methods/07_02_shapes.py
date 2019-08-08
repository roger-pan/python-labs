'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''

class rectangle:
    """Attributes of a rectangle"""
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

shape_1 = rectangle(5,10)
print(shape_1.area())

class circle:
    """Attributes of a circle"""

    def __init__(self,radius):
        self.radius = radius
        self.area = 3.14*self.radius



shape_2 = circle(5)
print(shape_2.area)