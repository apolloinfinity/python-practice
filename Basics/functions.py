#creating a function in Python
def f(x):
    return x * 2


result = f(3)

print(result)


def f(y):
    return y + 1


z = f(4)

if z == 5:
    print("Z is 5")
else:
    print("z is not 5")


def f(x, y, z):
    return x + y + z


result = f(1, 2, 3)
print(result)

# functions don't have to have a return statement but will give a message of none


def f():

    z = 1 + 1

    result = f()
    print(result)


# Built in functions

str = "Monty"
# len() function is equivilent of .length in Javascript
print(len(str))

#int function converts strings to integers and floating points to whole integers
number = int("1")

print(number)

num1 = int("20")
num2 = int(2023.01)

print(num1)
print(num2)

#float will convert numerical strings into floating points and convert whole integers to floating points

num3 = float("15.43")
num4 = float(99)

print(num3)
print(num4)


#input function
age = input("Enter your age:")
int_age = int(age)
if int_age < 21:
    print("You are young!")
else:
    print("Wow! You're old")


#Reusing functions

def even_odd(x):
    if x % 2 == 0:
        print("even");
    else:
        print("odd")

even_odd(2)
even_odd(3)

#Required and option paramaters

def f(x =2):
    return x**x

print(f())
print(f(4))

def add_it(x, y = 10):
    return x + y

result = add_it(2)
print(result)
