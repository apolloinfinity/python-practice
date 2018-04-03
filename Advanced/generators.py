"""
Generators are useful when iterating through large datasets. Because they are not lists and show only one result at a time, they are much faster and use less
memory than lists. The keyword used with generators is yield instead of return. More than one yield can be used inside of a function.
"""

# Simple example of a generator

def countdown():
    i = 5
    while i > 0:
        yield i
        i-=1

# Just tells you that there is a generator object
a = countdown()
# print(a) 

# This will return only one item from the generator list which is five. Printing print over and over will yield the results of the iteration. 
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))


# Here is a simpler way to do the above with a for loop

for i in countdown():
    print(i)

# Although it defeats the purpose of using generators, the generator results can be turned into a list.

print(list(a))

"""Using Generators on a string"""

def my_string():
    word = ""
    for ch in "Liopleurodon":
        word += ch
        yield word

print(list(my_string()))

    