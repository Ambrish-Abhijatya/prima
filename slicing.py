#my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0  1  2  3  4  5  6  7  8  9    Positive Indexes
#        -10 -9 -8 -7 -6 -5 -4 -3 -2 -1   Reverse Indexes
#list[start:end:step] 

'''print(my_list[0:])
print(my_list[1:7])    
print(my_list[1:8:1])         
print(my_list[-9:-3])
print(my_list[-7:7:-1])
print(my_list[7:-7:-1])
print(my_list[::-1])'''

my_url = 'https://python.com'

#print the url without the https://
print(my_url[8:])
#print the url without the top level domain or the https://
print(my_url[8:-4])
# print the top level domain
TLD_index = my_url.index('.')
print(my_url[TLD_index:]) #this is more readable than print(my_url[my_url.index('.'):])