"""
A Class is a blueprint for how an object should behave
classes start with a capital letter like objects in JS
classes first function(method) acts is a constructor like in JS.
"""

class Planet():
    def __init__(self):
        self.name = 'Hoth'
        self.radius = 20000
        self.gravity = 5.5
        self.system = 'Hoth System'


hoth = Planet()

print(hoth.name)
print('It\'s gravity is {} times more than Earth\'s'.format(hoth.gravity))