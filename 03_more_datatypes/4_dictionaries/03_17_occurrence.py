'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''
user_input = "hello"
result = {}
for x in user_input:
    result[x] = user_input.count(x)
print(result)