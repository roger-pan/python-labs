'''
Write a script that takes three strings from the user and prints the one with the most characters.

'''

input_string_1 = input("Input a string: ")
input_string_2 = input("Input another string: ")
input_string_3 = input("Input a final string: ")
list = [input_string_1, input_string_2, input_string_3]
print(max(list))