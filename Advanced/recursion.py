"""
A recursive function is a function that calls itself in the code. 
It has 2 parts. A base case andthe recursive case. If a recursive function doesn't have a base case, you can have an infinite loop.
"""

# Simple countdown recursive function.
"""def countdown(n):
    print(n)
    if n <= 0: # This is the base case.
        return
    else:
        return countdown(n-1) # This is the recursive case.

print(countdown(10))
"""
# Factorial recursive function.
"""
def fact(y):
    if y == 1:
        return 1 # Base case for this factorial
    else:
        return y * fact(y-1) # Recursive call

print(fact(5))
print(fact(10))
"""

def fib(x):
    if x == 0:
        return 0
    elif x <= 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

print(fib(6))