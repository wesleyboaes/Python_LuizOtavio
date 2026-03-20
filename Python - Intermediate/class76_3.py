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

person = {
    'name': 'Wesley',
    'last_name': 'Boaes',
    # 'age': 99,
}

person.setdefault('age', 99)
print(person['age'])
# print(len(person))
# print(person.keys())
# items = tuple(person.keys())
# print(items[0], items[1])
# print(list(person.keys()))
# print(list(person.values()))
# print(list(person.items()))

# for key in person:
#     print(key)
# for value in person.values():
#     print(value)

# for key, value in person.items():
#     print(key, value)