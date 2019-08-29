'''
Write a script with a function that demonstrates the use of *args.

'''

def my_function(*args):
    for i in args:
        print(i)

my_function(1,2,3,4,5)