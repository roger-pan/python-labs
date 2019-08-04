'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''

'''
number_1 = int(input("Input number: "))
number_2 = int(input("Input number: "))
number_3 = int(input("Input number: "))
number_4 = int(input("Input number: "))
number_5 = int(input("Input number: "))
number_6 = int(input("Input number: "))
number_7 = int(input("Input number: "))
number_8 = int(input("Input number: "))
number_9 = int(input("Input number: "))
number_10 = int(input("Input number: "))

number_list = [number_1,number_2,number_3,number_4,number_5,number_6,number_7,number_8,number_9,number_10]
'''

number_list = [1,2,3,4,5,6,7,8,9,10]

number_product = 1
for x in number_list:
    number_product = number_product * x
print(number_product)