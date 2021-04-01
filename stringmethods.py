message = 'Hello World'
#print(message.upper())
#print(message.lower())
'''for i in range(len(message)):
    print(message[i])''' #This is how we access individual characters in the list.
print("The number of times the substring 'Hello' occurs in the string 'Hello World' is:",message.count('Hello'))
print("The number of times the substring 'l' occurs in the string 'Hello World' is:",message.count('l'))
print("In 'Hello World', the first 'l' begins at index",message.find('l'))
print("In 'Hello World', 'World' begins at index",message.find('World'))
print('If we pass on a string that is not a substring in the find method, the output is:', message.find('Universe'))
#message.replace('World', 'Universe')
#print(message) #the replace method doesn't modify the original string 
'''new_message = message.replace('World', 'Universe') #But the replace method returns a new string with the replacements
print(new_message)'''
message = message.replace('World', 'Universe') #This is how we modify the object if the method doesn't
print(message)