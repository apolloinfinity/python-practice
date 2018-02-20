"""
I'm learning more how to be more "pythonic" with my python.
Learning how to use set() to remove repeat in a list and converting that set back to a list. 
"""

magicians = ['Houdini', 'Cooperfield', 'Dude with mask']
for magician in magicians:
    print(magician)

numbers = [1, 2, 2, 3, 4, 4, 44, 5, 6, 7 ,8, 8, 12, 12,]
set_numbers = set(numbers)
list_numbers = list(set_numbers)
print(list_numbers)

print(type(list_numbers))