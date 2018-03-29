import random as r

a = [43, 6, 46, 1, 50, 19, 21, 46, 11, 40, 20, 22, 50, 17, 14, 13, 6, 6, 33]

# for i in range(1, 20):
#     i = r.randint(1, 50)
#     new_arr.append(i)

# min method finds the smallest number in the list
print(min(a))

# max method finds the largest number in the list
print(max(a))

# abs method returns the the absolute value of a number. 
print(abs(-320))

# sum method adds all the numbers inside of a list together.
print(sum(a))

nums = (55, 44, 33, 22)
print(max(min(nums[:2]), abs(-42)))