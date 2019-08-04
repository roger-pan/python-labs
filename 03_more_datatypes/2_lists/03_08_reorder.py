'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input: 1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

'''

n = input("Enter list of 10 numbers separated by a space: ")
lst = n.split()
new_list = []
for x in lst:
    new_list.append(int(x))

print(new_list[1]) # Second number
print(new_list[3]) # Fourth number
print(new_list[5]) # Sixth number
print(new_list[7]) # Eighth number
print(new_list[9]) # Tenth number
print(new_list[8]) # Ninth number
print(new_list[6]) # Seventh number
print(new_list[4]) # Fifth number
print(new_list[2]) # Third number
print(new_list[0]) # First number


