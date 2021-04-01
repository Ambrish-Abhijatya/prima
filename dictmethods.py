planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initials = { planet : planet[0] for planet in planets}
planet_to_initials['Pluto'] = 'Pluto'[0]
print(planet_to_initials)
print(planet_to_initials['Venus'])
print('Saturn' in planet_to_initials)
print('Ganymede' in planet_to_initials)
for planet in planet_to_initials:
    print("{} = {}".format(planet.rjust(10), planet_to_initials[planet]))
zs = ' '.join(sorted(planet_to_initials.values()))  
print(zs)
for planet, initial in planet_to_initials.items():
    print('{} begins with {}'.format(planet.rjust(10), initial))