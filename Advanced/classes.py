"""
A Class is a blueprint for how an object should behave.
1. Class names must start a capital letter.
2. Is a reserved method for python classes and must be declared. It is a constructor that initializes the class
3. Methods are functions inside of classes. 
4. Created an instance of the Planet object with properties.
5. f' is a string formatter new to Python 3.6.
6. Class level attributes are put in the head of the class before the __init__ method. They are owned by the class itself. They have the same value for every class. In this example, all the planets are round.
"""
# 1. Declaring a class
class Planet():

    # 6. Class Level attributes
    shape = 'round'

    #. Creating the Initial method
    def __init__(self, name, radius, gravity, system):
        # 2. Class properties
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system
    
    # 3. Method
    def orbit(self):
        # 5. The f' is a formatter string literal.
        return f'{self.name} is orbiting in the {self.system}'


# 4. Creating an instance of the object
hoth = Planet('Hoth', 20000, 5.5, 'Hoth System')

print(f'Name is: {hoth.name}')
print(f'Radius is: {hoth.radius}')
# print('It\'s gravity is {} times more than Earth\'s'.format(hoth.gravity))
print(f'The gravity of {hoth.name} is {hoth.gravity} times more than Earth\'s.')
print(hoth.orbit())

naboo = Planet('Naboo', 300000, 8, 'Naboo System')
print(f'Name: {naboo.name}')
print(f'Radius: {naboo.radius}')
print(f'Gravity: {naboo.gravity}')
print(naboo.orbit())