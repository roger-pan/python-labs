'''

Write a script that completes the following tasks.

'''

# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean

def divisible_4_7(x):
    if x % 4 == 0 or x % 7 == 0:
        return True
    else:
        return False

# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean

def divisible_4_and_7(x):
    if x % 4 == 0 and x % 7 == 0:
        return True
    else:
        return False

# take in a number from the user between 1 and 1,000,000,000

number = int(input("Input a number between 1 and 1,000,000,000: "))

# call your functions, passing in the user input as the arguments, and set their output equal to new variables 

i = divisible_4_7(number)
j = divisible_4_and_7(number)

# print your new variables to display the results

print(i)
print(j)
