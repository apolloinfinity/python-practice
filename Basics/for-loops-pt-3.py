#You can nest loops in Python like you would in JavaScript.
for i in range(1,3):
    print(i)
    for letter in ["a", "b", "c"]:
        print(letter)
#First loop is the outer loop and the second loop is the inner loop.

#You can use a nested loop to add numbers from another list
list1 = [1,2,3,4]
list2 = [5,6,7,8]
added = []
for i in list1:
    for j in list2:
        added.append(i + j)
print(added)
