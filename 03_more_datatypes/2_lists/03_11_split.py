'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

input_string = str(input("Input a string: "))
lst = input_string.split()
word_counter = {}
for x in lst:
    if x in word_counter.keys():
        word_counter[x] += 1
    else:
        word_counter[x] = 1

print(max(word_counter,key = word_counter.get))


