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

for i in range(20, 30):
    print(i)

   
#While loops execute a block of code while the condition is true.
#Once the condition is false the while loop stops.
x = 10
while x > 0:
    print('{}'.format(x))
    x -= 1
print("Happy New Year!")

#This is an example of an infinite while-loop
#while True:
#    print("Hello World!")
    
#You can use the break-statement to terminate a loop
#The moment python hits the break-statement, the loop ends. 
for i in range(0, 100):
    print(i)
    break

qs = ["What is your name?",
      "What is your favorite color?",
      "What is your quest?"]
n = 0
while True:
    print("Type q to quite")
    a = input(qs[n])
    if a == "q":
        break
    n = (n + 1) % 3
