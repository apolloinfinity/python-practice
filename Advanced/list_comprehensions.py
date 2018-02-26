cubes = []
for value in range(1, 20):
    cubes.append(value ** 3)

print(cubes)

# Pythonic way is to do the above as a list comprehensions
# You start with a descriptive name of the list
# Then use square brackets and define the expression
# Then write a for loop to generate the numbers for cubed.

cubed = [value**3 for value in range(20, 30)]
print(cubed)

# Using list comprehensionto multiply by a number
multiply_2 = [value*2 for value in range(20)]
print(multiply_2)

multiply_2_even = [value*2 for value in range(20) if value%2==0]
print(multiply_2_even)

# Possibly doing FizzBuzz with list comprehension??
# This is my attempt. I will push this, even if it doesn't work

# FizzBuzz = [fizz, buzz for value in range(1,20)if value%3 == 0 and value%5==0]