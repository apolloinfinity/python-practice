# Large programs can be broken down to smaller programs called modules.
# Python allows you to use code from one module to another module.
# Python also has built-in modules. 

import math
import random
import statistics
import keyword

# This uses Math power module.
mthPow = math.pow(2, 3)
print(mthPow)

# This will create a random number every time the block of code is ran.
mthRndm = random.randint(0, 100)
print(mthRndm)

# mean
nums = [1, 5, 33, 12, 46, 33, 2]
print(statistics.mean(nums))

# median
print(statistics.median(nums))


# mode
print(statistics.mode(nums))


# There is a built-in module called keyword that checks if a string is a Python keyword.

print(keyword.iskeyword("for"))
print(keyword.iskeyword("football"))
