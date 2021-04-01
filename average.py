#create an everage function
'''def avg(nums):
    s = 0
    for num in nums:
        s+=num
    return s/len(nums)

l1 = [1 , 5, 7, 9]
print(avg(l1))'''


'''from functools import reduce

def sum_n(k):
    return reduce(lambda x, y: x+y, range(1, k+1))
print(sum_n(12))'''

'''def sum_of_first_n_numbers(n):
    s = 0
    for i in range(1, n+1):
        s+=i
    return s

print(sum_of_first_n_numbers(10))'''

#Exercise 1: Given two integer numbers return their product. 
# If the product is greater than 1000, then return their sum

'''def ex1_func(m, n):
    return m+n if m*n > 1000 else m*n

print(ex1_func(12,13))
print(ex1_func(1210,13))'''

#Exercise 2: Given a range of the first 10 numbers, 
#Iterate from the start number to the end number, 
#and In each iteration print the sum of the current number and previous number

'''for i in range(10):
    x = 0 if i==0 else i-1
    print(f'Current number = {i}, Previous Number = {x}, Sum = {x+i}, Product = {i*x}')'''

#Exercise 3: Given a string, display only those characters 
#which are present at an even index number.

'''def ex3_func(string):
    print(f'Original string is {string}.')
    print('Returning only even index characters: ')
    for i in range(len(string)):
        if i%2 == 0 and string[i] != ' ':
            print(string[i])

ex3_func(' Hello Jackass')'''

#Exercise 4: Given a string and an integer number n, 
#remove characters from a string starting from zero up to n 
# and return a new string

'''def ex4(al, n):
    return 'Too long slicing argument' if n > len(al) else al[n+1:]

print(ex4('Carpe Diem', 15))
print(ex4('Carpe Diem', 5))'''

#Given a list of numbers, return True if first and last number of a list is same

'''def ex5(l):
    return l[0] == l[-1]

print(ex5([1, 31, 11]))
print(ex5([1, 31, 1]))'''

#Exercise 6: Given a list of numbers, 
#Iterate it and print only those numbers which are divisible of 5

'''def exer6(iter):
    return [ i for i in iter if i%5==0]

print(exer6([5,15,25,11,165]))
print(exer6([1,2,3,4]))'''

#Exercise 7: Return the count of sub-string “Emma” appears in the given string
def ex7(string):
    return string.count('Emma')
print(ex7("Emma is good developer. Emma is a writer"))