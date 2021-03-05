'''print(print)
def hello_func():
    pass
print(hello_func)

def SayHi(Greeting= 'Hi' ,who = 'User'):
    return f'{Greeting} {who}!'

print(SayHi())
print(SayHi('Hello','Jack').upper())'''

def student_info(*args, **kwargs):
    print(args) #args are printed in a tuple
    print(kwargs) #kwargs or keyword arguments are printed in dictionary

student_info('Math', 'Art', name='John', age=22)

courses = ['Physics', 'CompSci', 'Anatomy']
info = {'name': 'Dominique', 'age': 21}
#student_info(courses, info)
student_info(*courses, **info) #can also go the other way around