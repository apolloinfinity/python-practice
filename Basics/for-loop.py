#For loop has a different syntax than that in JavaScript
#Where in JS you would do for(var i = 0; i < 5; i++){ do something }
#Python use the "in" keyword

name = "Ted"
for character in name:
    print(character)
    

#Here is an example of a for-loop iterating through a list with items
shows = ["GOT",
         "Westworld",
         "Brain Games"]
for show in shows:
    print(show)

#In the above example. The word "show" after for is defining the loop.

#Here is an example of using the for-loop in a dictionary
people = {"G. Bluth II":
          "A. Development",
          "Barney":
          "HYMYM",
          "Dennis":
          "Always Sunny"
          }

for character in people:
    print(character)

#In this example, the for-loop keeps track of items in a list using an index variable.
tv = ["GOT",
      "Narcos",
      "Vice"]
i = 0
for show in tv:
    new = tv[i]
    new = new.upper()
    tv[i] = new
    i += 1

print(tv)

#Accessing items in an index with an iterable is so common, python has another syntax for it
music = ["Machine",
         "Parabola",
         "Stillborn"]
for i, show in enumerate(music):
    new = music[i]
    new = new.upper()
    music[i] = new

print(music)


