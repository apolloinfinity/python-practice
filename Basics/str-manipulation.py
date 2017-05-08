author = "Kafka"

#Strings are immutable
ff = "F. Fitzgerald"

#String multiplication
multiStr = "Sawyer " * 3
print(multiStr)

#making all letters in a string uppercase with uppercase method
#making all letters lowercase with the lowercase method
#capitalizing the first word of a sentence
str = "We hold these truths...."

print(str.upper())
print(str.lower())
print("the cat jumped over the moon... or cow".capitalize())


#format method can create new strings in a string by using curly braces
str = "William {}".format("Faulkner")

last = "Gibson"
str2 = "William {}".format(last)

#format method's curly braces can be used more than once.

author = "William Gibson"
book = "Neuromancer"

sprawl = "{} wrote {}".format(author, book)

#Python has a split method. Split method seperates a string into many strings
#In JS it creates a list from it and list methods can be used on it.

str3 = "The fox jumped over the fence"

#Python also has a join method that joins together a list of strings into one

words = ["The",
         "forx",
         "jumped",
         "under",
         "the",
         "moon",
         "."]

one = "".join(words)
oneS = " ".join(words)
print(one)
print(oneS)

#You can also strip leading or trailing whitespace off a string using strip method

s = "                   The      "
s = s.strip()
print(s)

#You can also find an index of the first occurence for a character in a string.

indStr = "animals".index("m")
print(indStr)

#If the index method doesn't find a character, python raises an exception

#indStr = "animals".index("z")
#print(indStr)


#In keyword checks to see if a string is found inside of another string and returns true or false.

#Slice method returns a new lists that can be itereable.
#It has a start and end index. Start is where you want the slice to begin
#End index is where you want the slicing to end.

fict = ["Tolstoy",
        "Camus",
        "Orwell",
        "Huxley",
        "Austin"]
print(fict[0:3])

ivan = """In place of death there was light."""
print(ivan[0:17])
print(ivan[17:33])

#You can leave the index empty if you the index is the last item of iterable
