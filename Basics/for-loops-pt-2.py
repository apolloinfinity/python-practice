#You can use multiple loops and append then to one list like this example.
tv = ["GOT", "Narcos",
      "Vice"]
coms = ["Arrested Development",
        "Friends",
        "Always Sunny"]
all_shows = []

for show in tv:
    show.upper()
    all_shows.append(show)

for show in coms:
    show = show.upper()
    all_shows.append(show)

print(all_shows)

#range is a built-in function that can create a sequence of characters.
#rang takes to parameters. A number of where to start and a number where to stop.

for i in range(1,20):
    print(i)

