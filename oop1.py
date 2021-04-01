class Employee:

    raise_amount = 1.04
    num_of_emps = 0
    
    def __init__(self, first, last, pay): #initializing class attributes
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@pirate.com'
        Employee.num_of_emps+=1

    def fullname(self):          #creating a class method
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)       #can also use Employee.raise_amount since a class variable can be accessed its class
        
'''Remember : Each method within a class automatically takes in
   the instance variable as the first argument by convention we
   call the instance as self'''


emp_1 = Employee('Jack', 'Sparrow', 50000)
emp_2 = Employee('Test', 'User', 60000)

#print(emp_1)
#print(emp_2)

print(emp_1.email)
print(emp_2.email)


'''when we call the method on an instance we don't need to  
   pass in the instance variable, it is done automatically.'''
print(emp_2.fullname())  
'''However when we call the method on the class, then the instance on which the
   method is to be run, is ambiguous hence we have to pass an instance '''
print(Employee.fullname(emp_1)) 

#We can access the class variable from the class itself as well as from both instances
#That brings us to the defining property of class variables, they are shared among all
#instances of a class, and are not unique attributes to a particular instance

'''print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)'''

'''print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)'''

#print(emp_1.__dict__)
#print(emp_2.__dict__)
#print(Employee.__dict__)

#Employee.raise_amount = 1.05
#emp_1.raise_amount = 1.05
#print(emp_1.__dict__)
#print(Employee.raise_amount)
#print(emp_1.raise_amount)
#print(emp_2.raise_amount)

print(Employee.num_of_emps)
