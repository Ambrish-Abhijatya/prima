# collections: Counter, namedtuple, ordered_dict, default_dict, deque
from collections import Counter
a = 'aaabbc'
my_counter = Counter(a)
print(my_counter)
#print(my_counter.items())
#print(my_counter.keys())
#print(my_counter.values())
print(my_counter.most_common(1))
print(my_counter.most_common(2))
print(my_counter.most_common(2)[1][1])