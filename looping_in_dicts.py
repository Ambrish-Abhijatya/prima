student = {'name' : 'John', 'age' : 25, 'courses' : ['Maths', 'CompSci']}
#print(student)
#print(len(student))
#print(student.keys())
#print(student.values())
#print(student.items()) #returns key value pairs in a list of tuples

for key in student:   #looping through a dictionary by default is looping through its keys
    print(key)        #ie we don't need to add the keys() method

print('\n')

for value in student.values():
    print(value)

print('\n')

for key, value in student.items():
    print(key, ' = ', value)
