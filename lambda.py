'''def double(x):
    return x*2

def add(x, y):
    return x + y

def product(x, y, z):
    return x*y*z'''

'''double = lambda x : x * 2
add = lambda x, y : x + y
product = lambda x, y, z : x * y * z 

print(double(3.5))
print(product(5, -1, 7))
print(add(73,-72))'''

#map, filter and reduce

my_list = [2, 5, 8, 10, 9, 3]
a = map(lambda x : x * 2, my_list)  # map(function, iterable)
#print(a)
#print(list(a))
#print(my_list, 'with each entry doubled is', list(a))
print(f'{my_list} with each entry doubled is {list(a)}.')

my_list2 = [1, 4, 7, 8, 5, 1]
b = map(lambda x, y : x + y, my_list, my_list2)
#print(list(b))
print(f'The list with entrywise sums of the lists {my_list} and {my_list2} is {list(b)}.')

c = filter(lambda x : x % 2 == 0, my_list)         #filter(function with boolean return value, iterable)
#print(list(c)) #only the entries in the iterable which return True in the function get filtered through
print(f'The list of even entries in the list {my_list} is {list(c)}.') 

d = filter(lambda x : x >= 5, my_list)
print(f'The list of values greater than or equal to 5 in the list {my_list} is {list(d)}.')

from functools import reduce

e = reduce(lambda x, y : x + y, my_list)
print(my_list , e)

l1 = [4, 3, 2, 1]

'''l2 = []      #Traditional Way
for x in l1:
    l2.append(x**2)'''

'''print([x**2 for x in l1])      #Syntactic Sugar(Python list comprehension)'''

# using lambda functions and map
print(f'The list {l1} with each entry squared becomes {list(map(lambda x : x**2, l1))}.')

def factorial(n):
    return reduce(lambda x, y : x * y, range(1,n+1))

print(factorial(5))