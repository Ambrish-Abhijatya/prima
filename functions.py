def SayHello():                                             #function  defintion
    print("Hello", input("Enter your name: "), "!")        

SayHello()                                                  #function call 

def SayHi(name = "User"):
    print("Hi", name, "!")

SayHi()
SayHi("Jack")

'''def least_difference(a, b, c):
    """Return the smallest difference
       between any two numbers among
       a, b and c.
    >>> least_difference(1,4,-5)
    3
    """
    return min(abs(a-b), abs(b-c), abs(a-c))

#help(least_difference)
print(least_difference(1,400,-5))'''