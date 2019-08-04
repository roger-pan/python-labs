'''
Write a script prints the number of times a vowel is used in a user inputted string.

'''

vowels = ["a","e","i","o","u"]

string_input = input("Input a string: ")
count = 0
for i in string_input:
    for j in vowels:
        if i == j:
            count +=1
print(count)