#list

fruit = list()
print(fruit)

fruit = []

fruit = ["Apple", "Orange", "Pear"]
print(fruit)

fruit.append("Banana")
fruit.append("Peach")

print(fruit)

#accessing the index of a list
print(fruit[3])

#list are mutable, so objects can be added or removed.

colors = ["blue", "green", "yellow"]
print(colors)
colors[2] = "red"
print(colors)

colors = ["blue", "green", "yellow"]
print(colors)
item = colors.pop()
print(item)
print(colors)


colors1 = ["blue", "green", "yellow"]
colors2 = ["orange", "pink", "black"]

#write colors1 + colors2 in the shell

#you can check to see if an item is in a list with the keyword in:
colors1 = ["blue", "green", "yellow"]
#write "green" in colors1 in the python shell


#Tuples are lists that are immutable. Meaning that you can't add or delete objects inside a tuple.
my_tuple = tuple()
