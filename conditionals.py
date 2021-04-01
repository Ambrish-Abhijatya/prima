# difference between == and 'is' comparison operators
a = [1, 2, 3]
b = [1, 2, 3]
print(f'id(a) = {id(a)} and id(b) = {id(b)}')
print('If a and b have same values but different id\'s (this has something to do with memory allocation) then a == b evaluates to' ,a == b)
print('But \'a is b\' evaluates to :' ,a is b)
a = b
print(f'id(a) = {id(a)} and id(b) = {id(b)}')
print( 'Whereas when a and b have the same id\'s \'a is b\' evaluates to:',a is b)

# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.
    # Any empty set. For example, set()
condition = {}
if not(condition):
    print('Evaluated to False')
else:
    print('Evalated to True')