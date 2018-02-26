from planet_class import Planet 

naboo = Planet('Naboo', 300000, 8, 'Naboo System')
print(f'Name: {naboo.name}')
# print(f'Radius: {naboo.radius}')
# print(f'Gravity: {naboo.gravity}')
# print(naboo.orbit())
print(Planet.shape)
# print(naboo.commons())
print(Planet.spin(4000))