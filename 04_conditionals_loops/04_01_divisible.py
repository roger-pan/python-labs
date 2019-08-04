'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''

input_number = int(input("Input a number between 1 and 1,000,000,000: "))
if input_number % 3 == 0:
    print(input_number / 3)
else:
    print("Not divisible by 3")