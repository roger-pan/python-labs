'''
Write a script that sorts a list of tuples based on the number value in the tuple.
For example:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

'''
unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
order = {}
sorted_list = []
list_length = len(unsorted_list)
# Bubble sort based on index 1 for each tuple
for i in range(list_length):
    for j in range(0,list_length - i -1):
        if unsorted_list[j][1] > unsorted_list[j+1][1]:
            unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]
print(unsorted_list)

