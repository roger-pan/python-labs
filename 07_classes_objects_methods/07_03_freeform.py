'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets attributes
    to a default value if values are not passed.
- Create at least two objects of each class using the __init__ method.
- Each object should have at least three attributes.
- Each class should have at least two class attributes.
- Create a print method in each class that prints out the attributes
    in a nicely formatted string.
- Include a __str__ method in each class.
- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator.
- Once the objects are created, change some of the attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, poker games, sports teams, trees, beers, people etc...


'''

# Creating a class called hat
class hat:
    """Attributes of a hat"""

    body_part = "head"
    price = 5

# Initialising hat
    def __init__(self,brand = "generic",colour = "black", pattern = "plain"):
        self.brand = brand
        self.colour = colour
        self.pattern = pattern
# Calling __str__
    def __str__(self):
        return f"This is a {self.pattern} {self.colour} {self.brand} hat"

    def __add__(self, other):
        return "You've got two hats"


hat_1 = hat("Nike","white","plain")
print(hat_1)
hat_2 = hat("Adidas","yellow","spotted")
print(hat_2)
print(hat.body_part)
print(hat.price)
print(hat_1 + hat_2)