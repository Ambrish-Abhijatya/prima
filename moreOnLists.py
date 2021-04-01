from lists import Mathematicians
LesMathematiciens = ["Gauss", "Euler", "Archimedes", "Newton", "Euclid", "Ramanujan", "Lobachevsky"]
LesPhyscicistes = ["Feynman", "Hawking", "Boltzmann", "Penrose"]
LesMathematiciens.extend(LesPhyscicistes)
print(LesMathematiciens)
LesPhyscicistes.insert(1, "Coulomb") #index function has two arguments
print(LesPhyscicistes)
LesPhyscicistes.remove("Coulomb")
print(LesPhyscicistes)
LesPhyscicistes.pop() #pop removes the last element by default
print(LesPhyscicistes)
#LesPhyscicistes.clear() #empties the list
LesPhyscicistes.sort() #sorts the list in alphabetical/ascending order
print(LesPhyscicistes)
Mathematicians.reverse() #Reverses the order of the list
print(Mathematicians)