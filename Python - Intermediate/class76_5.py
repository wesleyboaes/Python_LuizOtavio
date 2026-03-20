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

p1 = {
    'name': 'Wesley',
    'last_name': 'Boaes',
}
# print(p1.get('name'))

# name = p1.pop('name')
# print(name)
# print(p1)

# last_key = p1.popitem()
# print(last_key)
# print(p1)

# p1.update({
#     'name': 'Maiara',
#     'age': 35,
# })
# p1.update(name = 'Maiara', age = 35)
tuple = (('name', 'Maiara'), ('age', 35))
list = [['name', 'Maiara'], ['age', 35]]
# p1.update(tuple)
p1.update(list)
print(p1)