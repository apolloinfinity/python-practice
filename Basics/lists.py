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

# for value in range(1, 230):
#     print(value)

# Skipping Numbers
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# Creating squares with for loop and range method
squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)

print(squares)

# More consise way of writing the same problem above
squared = []
for val in range(1,11):
    squared.append(val**2)

print(squared)

# More pythonic way of doing the same problem as a list comprenhension
squareds = [value**2 for value in range(1,14)]
print(squareds)