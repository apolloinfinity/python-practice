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

locations = []

la = (34.0522, 188.2437)
chicago = (41.8781, 87.6298)

locations.append(la)
locations.append(chicago)

print(locations)

#This container contains a list, a tuple, and a dictionary

ny = {"location":
      (40.7128,
       74.0059),

      "celebs":
      ["W.Allen",
       "Jay Z",
       "K. Bacon"],

      "facts":
      {"state":
       "NY",
       "country":
       "America"}
}
