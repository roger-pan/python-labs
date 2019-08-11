'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''

file = 'words.txt'
with open(file,'r') as words:
    contents = words.read().split()
    reverse_contents = []
    for each in range(len(contents) - 1,-1,-1):
        reverse_contents.append(contents[each])

print(reverse_contents)
reverse_file = 'words_reverse.txt'
with open(reverse_file,'w') as words:
    words.write("\n".join(reverse_contents))




