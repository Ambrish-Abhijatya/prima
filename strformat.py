planet = 'Pluto'
pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
#         2 decimal points   3 decimal points, format as percent     separate with commas
print(
'''{} weighs about {:.2} kilograms ({:.3%} of earth\'s mass). 
It is home to {:,} plutonians.'''.format(planet, pluto_mass, pluto_mass/earth_mass, population)
)
#Referring to format() arguments by index starting from 0
print('Pluto is a {0}.\nNo it\'s a {1}.\n{0}!\n{1}!'.format('planet', 'dwarf planet'))