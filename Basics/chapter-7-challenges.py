#1. Print each item in the following lists. ["The Walking Dead", "Entourage", "The Sopranons", "The Vampire Diaries"]
shows = ["The Walking Dead", "Entourage", "The Sopranons", "The Vampire Diaries"]

for show in shows:
    print(show)

#2. Print all the numbers from 25 to 50
for i in range(25, 50):
    print(i)

#3.Print each item in the list from the first challenge and their indexes.
for i, a in enumerate(["The Walking Dead", "Entourage", "The Sopranons", "The Vampire Diaries"]):
    print "'%s is %d'" % (a, i)
    
