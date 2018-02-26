class Car():
    wheel_shape = 'round'

    def __init__(self, engine, wheels, color, powertrain):
        self.engine = engine
        self.wheels = wheels
        self.color = color
        self.power = powertrain

    def isElectric(self):
        if self.engine == 'Electric'.lower():
            return 'You\'re car must be made my Tesla'
        else:
            return 'What octane rating do you use?'

f430 = Car('v8', 4, 'cream', 'gasoline')
print(f430.isElectric())

model_s = Car('electric', 4, 'red', 'none')
print(model_s.isElectric())
print(Car.wheel_shape)