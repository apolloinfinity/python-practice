"""Python decorators are what makes Python so robust.
Decorators are functions that modify other functions.
It's idead if you don't want to modify functions. 
"""

def decor(func):
    
    # This inside function is what will be the decorator
    def wrap(): 
        print("=============")
        func()
        print("=============")

    # decor() returns wrap function
    return wrap

# This is the function I want decorated
def my_text():
    print("Hello Matey!")


# Declared a variable and assigned it the decor function with the function I want decorated. 
decorated = decor(my_text)

print(decorated())

# Python provides support for decoraor with the '@' symbol preceded with the name of the decorator
@decor
def print_more():
    print('Chewbacca is awesome!')

print(print_more())

""" Using decorators with numbers"""
def square_everything(func):
    def wrap():
        return func()**2

    return wrap

def cube_everythin(func):
    def wrap():
        return func()**3
    return wrap

@square_everything


def my_maths():
    return 5


print(my_maths())

# @cube_everythin
# def more_maths():
#     return 5

# print(more_maths())

