'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

'''

num_1 = input("Input a number: ")
num_2 = input("Input another number: ")

try:
    float(num_1)/float(num_2)
except ValueError:
    print("Inputs must be numbers")
except ZeroDivisionError:
    print("You can't divide by zero")
else:
    print(float(num_1)/float(num_2))


