'''print("alpha", "beta", "gamma", sep=' then ')
print(1, 2, 3, sep=' < ')


def greet(who = "Judas"):
    print("Hello", who)

greet() #Returns default
greet(who = "Jack") # Don't need to specify the name of the argument since it is unambiguous
greet("Sam") 

def mult_by_5(x):
    return 5*x

def call(fn, arg):
    return fn(arg)

def squared_call(fn, arg):
    return fn(fn(arg))

print(
    call(mult_by_5, 1),
    squared_call(mult_by_5, 1), 
    sep='\n'
    )
    

def mod_5(x):
    return x%5

print(
    "Which is the biggest number among 14, 401, and 5000?", 
    max(14, 401, 3000),
    "Which is the biggest number among 14, 401, and 5000 modulo 5?",
    max(14, 401, 3000, key = mod_5),
    sep='\n'
)'''

print("alpha", "beta", "gamma", end=' then ')
help(any)