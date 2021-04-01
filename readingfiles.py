employee_file = open("employees.txt", "r") # r- read, w- write, r+ - read&write, a- append

#print(employee_file.readable()) #Gives a boolean value accordingly as the file could be read or not.
#print(employee_file.read()) # Displays all the lines
#print(employee_file.readline()) # This function moves the cursor to the next line after executing.
#print(employee_file.readline())
#print(employee_file.readline())
#print(employee_file.readlines()) #Puts each line of the file as items in an array.
for employee in employee_file.readlines():
    print(employee) 

employee_file.close()         #A file that is opened must be closed at sometime.