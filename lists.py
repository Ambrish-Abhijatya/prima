LesMathemateciens = ["Gauss", "Euler", "Archimedes", "Newton"]
print(LesMathemateciens)
print(LesMathemateciens[0])
LesMathemateciens.append("Ramanujan")  #adds an item at the end
print(LesMathemateciens)
print(LesMathemateciens[-2])
print(LesMathemateciens[:-2])
LesMathemateciens[4] = "Lobachevsky" #lists are mutable
print(LesMathemateciens)
Mathematicians = LesMathemateciens.copy()
Mathematicians.insert(0, 'Ramanujan')  # adds an item on a specific index
print(Mathematicians)
