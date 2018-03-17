"""
Tuple Unpacking.
Tuple unpacking is a way to asign 2 or more variables to an equal amount of values 
For example:
a,b = b,a
"""

lax_coordinates = (33.9425, -118.408056) # coordinates are inside of a tuple

latitude, longitude = lax_coordinates # Two variables, latitude and longitude will get assigned to the two variables inside of lax coordinates

print(latitude)
print(longitude)