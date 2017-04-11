#if/else statements with strings
home = "America"
if home == "America":
    print("Hello, America!")
else:
    print("Hello, World!")

# multiple ifs with integers
x = 2
if x == 2:
    print("The number is 2.")
if x % 2 == 0:
    print("The number is even.")
if x % 2 != 0:
    print("The number is odd")

#assigning multiple variables and usin in an if statement
x = 10
y = 11

if x == 10:
    if y == 11:
        print(x + y)

#elif statement in which a variable matches a condition
home = "Thailand"
if home == "Japan":
    print("Hello Japan!")
elif home == "Thailand":
    print("Hello Thailand!")
elif home == "India":
    print("Hello India!")
elif home == "China":
    print("Hello, China")
else:
    print("Hello, World!")

#elif statement in which the variable doesn't match the condition
home = "Mars"
if home == "Japan":
    print("Hello Japan!")
elif home == "Thailand":
    print("Hello Thailand!")
elif home == "India":
    print("Hello India!")
elif home == "China":
    print("Hello, China")
else:
    print("Hello, World!")


#for loop in Python

for i in range(100):
    print("Hello, World!")
