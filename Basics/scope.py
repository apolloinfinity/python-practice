#variables in the global scope

x = 1
y = 2
z = 3

def f():
    print(x)
    print(y)
    print(z)

f()

#Like JS, defining variables inside a function makes them local to the functions scope

def f():
    x = 4
    y = 5
    z = 6
    print(x)
    print(y)
    print(z)

f()

#changing the value of a global variable inside of function requires an extra step

x = 100

def f():
    global x
    x += 1
    print(x)

f()
