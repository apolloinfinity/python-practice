"""
A recursive function is a function that calls itself in the code. 
It has 2 parts. A base case andthe recursive case. If a recursive function doesn't have a base case, you can have an infinite loop.
"""

# Simple countdown recursive function
def countdown(n):
    print(n)
    if n <= 0: # This is the base case
        return
    else:
        countdown(n-1) # This is the recursive case

print(countdown(100))