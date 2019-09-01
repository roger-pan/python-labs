'''
Write a decorator function that wraps text passed to it in a specified html tag.
The user should be able to decide which tag to use.

'''

def decorator_func(html_tag):
    def wrapper_func():
        print("html tag text: " + html_tag)
    return wrapper_func

variable = decorator_func("<html>")
variable()