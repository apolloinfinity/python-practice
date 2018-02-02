"""
A Class is a blueprint for how an object should behave
classes start with a capital letter like objects in JS
classes first function(method) acts is a constructor like in JS.
You will see in the print function and orbit method, the letter f.
It is new to Python 3.6 and it a formatted string literal. It can 
also be used for formatting as I have done in this examples.
"""

class Planet():
    def __init__(self, name, radius, gravity, system):
        # This are properties
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system
    
    # This is a method
    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'


hoth = Planet('Hoth', 20000, 5.5, 'Hoth System')

print(f'Name is: {hoth.name}')
print(f'Radius is: {hoth.radius}')
# print('It\'s gravity is {} times more than Earth\'s'.format(hoth.gravity))
print(f'The gravity of {hoth.name} is {hoth.gravity} times more than Earth\'s.')
print(hoth.orbit())

naboo = Planet('Naboo', 300000, 8, 'Naboo System');
print(f'Name: {naboo.name}')
print(f'Radius: {naboo.radius}')
print(f'Gravity: {naboo.gravity}')
print(naboo.orbit())