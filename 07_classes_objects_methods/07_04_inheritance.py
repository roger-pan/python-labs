'''
Build on the previous exercise.

Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in the previous exercise.

If you cannot think of a way to build on your previous exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

'''

class food:
    """Attributes of food"""
    def __init__(self, name = "None",meal="lunch",colour = "None" ):
        self.name = name
        self.meal = meal
        self.colour = colour

    def __str__(self):
        return f"You should eat {self.name} for {self.meal} "

class fruit(food):
    """Sub class of food"""

    def __init__(self,name,meal,colour,taste):
        super().__init__(name,meal,colour)
        self.taste = taste

    def __str__(self):
        return f"You should eat {self.name} with your {self.meal}"

print(fruit("tomato","lunch","red","yummy"))

class tomato(fruit):
    def __init__(self,name,meal,colour,quantity):
        super().__init__(name,meal,colour,quantity)
        self.quantity = quantity


    def chop(self):
        self.quantity *= 2



fruit_1 = tomato("Cherry","lunch","red",5)
print(fruit_1.quantity)
fruit_1.chop()
print(fruit_1.quantity)



