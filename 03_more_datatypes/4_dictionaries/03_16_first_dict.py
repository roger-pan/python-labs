'''
Write a script that creates a dictionary of keys, n and values n*n for numbers 1-10. For example:

result = {1: 1, 2: 4, 3: 9, ...and so on}

'''


list_numbers = [1,2,3,4,5]
dict_numbers = {}
for x in list_numbers:
    dict_numbers[x] = x**2
print(dict_numbers)
