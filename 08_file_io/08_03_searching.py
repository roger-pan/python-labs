'''
Write a script that searches a folder (and all its subfolders) on your computer and compiles a list of
all .jpg files. The list should contain the complete path of each .jpg file.

If you are feeling bold, create a list containing each type of file extension you find in the folder.

Start with a small folder to make it easy to check if your program is working correctly. Then switch that
small folder name with a bigger folder. This program should work for any specified folder on your computer.

'''
import os
path = '/Users/Roger/Downloads'
directory = os.walk(path)
print(directory)

jpg_file = []
for r,d,f in directory:
    for file in f:
        if ".jpg" in file:
            jpg_file.append(os.path.join(r,file))

print(jpg_file)