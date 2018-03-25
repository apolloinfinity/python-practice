"""
Tuple Unpacking.
Tuple unpacking is a way to asign 2 or more variables to an equal amount of values 
For example:
a,b = b,a
d,e,f = f,e,d
"""

lax_coordinates = (33.9425, -118.408056) # coordinates are inside of a tuple

latitude, longitude = lax_coordinates # Two variables, latitude and longitude will get assigned to the two variables inside of lax coordinates

print(latitude)
print(longitude)

# Using tuple unpacking with a function
# To use tuple unpacking with a function, you would use a star "*" inside of the arguments

def multiply(x,y):
    return x*y

z = (3,4)

print(f'Unpacking with tuples:{multiply(*z)}') 

# Asterisk (*) can also be used to grab excess items of variable

a, b, *rest = range(5) # range exceeds 3 variabls
print(a,b,rest) # what gets printed out is 0, 1, [2, 3, 4]

# More examples 

a, *body, c, d = range(5) # The star operator can be assigned in position of the list of variables.
print(a, body, c, d) # But can only be assigned to 1 operator

# *a, *head, c, d = range(10) """ This will cause an error"""
# print(a, head, c, d)

# Nested tuple unpacking

metro_areas = [
    ("Tokyo", "JP", 36.933, (35.689722, 139.691667)),
    ("Delhi NCR", "IN", 21.935, (28.613889, 139.691667)),
    ("Mexico City", "MX", 20.142, (19.433333, -99.133333)),
    ("New York-Newark", "US", 20.104, (40.808611, -74.020386)),
    ("Sao Paulo", "BR", 19.649, (-23.547778, -46.635833)),
]

print('{:15}')