'''
Demonstrate the use of the .enumerate() function.
'''

locations = ["Indonesia", "Spain", "Thailand", "Mexico", "USA"]
print(enumerate(locations))

my_list = ["apple", "banana", "orange"]
new_list = []
for index, value in enumerate(my_list):
    new_list.append(tuple([index,value]))

print(new_list)