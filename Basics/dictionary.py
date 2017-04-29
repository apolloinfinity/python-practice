#Dictionaries are another built in container that stores objects
#They are used to link one object(key) to another object(value)
#This is called mapping and it results in a key-value pair.
#Keys can be used to look up a value but a value cannot be used to look up a key.
#Dictionaries do not store their objects in a specific order like lists or tuples do.

#creating a dictionary.
my_dict = dict()

#Adding key-value pairs to a dictionary
fruits = {"Apple":
          "Red",
          "Banana":
          "Yellow"}
#Dictionaries are mutable
facts = dict()

#add a value
facts["code"] = "fun"

#the in keyword and not in can be used in dictionaries
bill = dict({"Bill Gates":
             "charitable"})
             
books = {"Dracula": "Stoker",
       "1984": "Orwell",
       "The Trial": "Kafka"}


#small program using a dictionary

rhymes = {"1": "fun",
          "2": "blue",
          "3": "me",
          "4": "floor",
          "5": "lives"
          }

n = input("Type a number:")
if n in rhymes:
    rhyme = rhymes[n]
    print(rhyme)
else:
    print("Not found")


#like JavaScript with multi-dimensional arrays, containers can be inside containers.

lists = []
rap = ["Tupac Shakur",
       "Eminem",
       "Jedi Mind Tricks",
       "Hopsin"]

rock = ["Pantera",
        "Amon Amarth",
        "Trivium",
        "Monuments"]

classical = ["Mozart",
             "Vivaldi",
             "Bach",
             "Beethoven"]

lists.append(rap)
lists.append(rock)
lists.append(classical)
print(lists)
