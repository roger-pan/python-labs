'''
Write a script that generates an exception. Handle this exception with a try/except.
For example:

list_ = ["hello world!"]
print(list_[1])

This raises and exception that needs to be handled.

'''
list_ = ["hello world!"]
try:
    print(list_[1])
except IndexError:
    print("This index does not exist")
except Exception as e:
    print(e)
