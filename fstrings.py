greeting = 'Hello'
name = 'Jack'
# instead of using the str.format() we can use fstrings
#message = '{} {}!, Welcome'.format(greeting, name)
#print(message)
message = f'{greeting} {name}!, Welcome.' 
print(message)
#we can also write code directly into the curly braces
message = f'{greeting} {name.upper()}!, Welcome.' 
print(message)