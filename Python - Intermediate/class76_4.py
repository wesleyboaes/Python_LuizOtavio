# Useful dictionary methods in Python
# len - how many keys
# keys - iterable with keys
# values - iterable with values
# items - iterable with keys and values
# setdefault - add values if key doesn't exist
# copy - return a shallow copy
# get - obtain a key
# pop - Delete an item with a specified key
# update - Updates one dictionary with another
import copy # Deepcopy

d1 = {
    'k1': 1,
    'k2': 2,
    'l2': [0, 1, 2], # Mutable
}

# d2 = d1
# d2['k1'] = 1000
# print(d1)

# d2 = d1.copy() # Shallow copy
d2 = copy.deepcopy(d1)
d2['k1'] = 1000
d2['l2'][1] = 999999
print(d1)
print(d2)