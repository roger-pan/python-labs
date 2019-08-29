'''
Write a script with a function that demonstrates the use of **kwargs.

'''

def my_function(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

my_function(item1='hi', item2='hello')