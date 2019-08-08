'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''

class car:
    """Models a car including its model, year and max speed"""
    def __init__(self,model,year,max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def increase_speed(self):
        self.max_speed += 5

    def __str__(self):
        return self.model


car_1 = car("Ford",1995,80)
print(car_1)
print(car_1.max_speed)
car_1.increase_speed()
print(car_1.max_speed)

car_2 = car("BMW",2019,130)
print(car_2)
print(car_2.max_speed)
car_2.increase_speed()
print(car_2.max_speed)
