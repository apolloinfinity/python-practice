"""
A Class is a blueprint for how an object should behave.
1. Class names must start a capital letter.
2. Is a reserved method for python classes and must be declared. It is a constructor that initializes the class
3. Methods are functions inside of classes. 
4. Created an instance of the Planet object with properties.
5. f' is a string formatter new to Python 3.6.
6. Class level attributes are put in the head of the class before the __init__ method. They are owned by the class itself. They have the same value for every class. In this example, all the planets are round.
7. A class method is a method that can only be used and points to the class itself. It cannot modify object instance state.
8. A static method takes neither self or cls parameter and are restricted to the data they can access.  
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
    
    # 7. Decorator and Class Method
    @classmethod
    def commons(cls):
        return f'All Planets are {cls.shape} because of gravity'

    # 8. Static Method
    @staticmethod
    def spin(speed = '2000 miles per hour'):
        return f'The planet spins and spins at {speed}'


# 4. Creating an instance of the object
naboo = Planet('Naboo', 300000, 8, 'Naboo System')
# print(f'Name: {naboo.name}')
# print(f'Radius: {naboo.radius}')
# print(f'Gravity: {naboo.gravity}')
# print(naboo.orbit())
# print(Planet.shape)
# print(naboo.commons())
print(Planet.spin(4000))