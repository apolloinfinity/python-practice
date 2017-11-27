# first few terms of the fibonacci sequence: 1,1,3,5 8, 13, 21

# def fibonacci(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     elif n > 1:
#         return fibonacci(n-1) + fibonacci(n-2)
#
# for n in range(1, 101):
#     print(n, ":", fibonacci(n))

fibonacci_cache = {}


# def fibonacci(n):
#     # If we have the cached value, then return it
#     if n in fibonacci_cache:
#         return fibonacci_cache[n]
#     # Computer the Nth term
#     if n == 1:
#         value = 1
#     elif n == 2:
#         value = 1
#     elif n > 2:
#         value = fibonacci(n-1) + fibonacci(n-2)
#
#     # Cached the value and return it
#     fibonacci_cache[n] = value
#     return value
#
#
# for n in range(1, 1001):
#     print(n, ":", fibonacci(n))

from functools import lru_cache


@lru_cache(maxsize=1000)
def fibonacci(n):
    # Check that the input is a positive integer
    if type(n) != int:
        raise TypeError("N must be a positive integer!")
    if n < 1:
        raise ValueError("n must be a positive integer")

    # Compute the Nth term
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 1:
        return fibonacci(n-1) + fibonacci(n-2)


for n in range(1,51):
    print(fibonacci(n))

