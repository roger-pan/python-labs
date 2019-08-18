'''
Write a script that demonstrates a try/except/else.

'''

words = input("Input 5 words of your choice (separated by a space): ")
lst = words.split()

# Test to see whether the user enters more than 5 words

try:
    print(lst[5])
except IndexError:
    print("There are 5 or less words")
else:
    print("There are more than 5 words")