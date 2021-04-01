cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
art_courses = {'History', 'Math', 'Art', 'Design'}
print(cs_courses) #sets are unordered and throw away repetitions
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second) #union
print(first & second) #intersection
print(first - second) #difference
print(second - first) #difference
print(first ^ second) #symmetric difference

#empty lists
empty_list = []
empty_list = list()

#empty tuples
empty_tuple = ()
empty_tuple = tuple()

#empty sets
empty_set = {} #This is WRONG, it creates an EMPTY DICTIONARY.
empty_set = set() #THIS is how we create an empyt set.
print(dir(first))