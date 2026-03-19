# Dictionaries in Python (dict type)
# Dictionaries are data structures of type "curly brackets" pair and "value"
# Curly Brackets can be considered as an "index" like we saw in list, and they can be of immutable types as: str, int, float, bool, tuple, etc.
# The value can be of any type, including another dictionary.
# We use curly brackets - {} - or the dict class to create dictionaries.
# Immutables: str, int, float, bool, tuple
# Mutable: dict, list

# person = {
#     'name': 'Wesley',
#     'last_name': 'Boaes',
#     'age': 34,
#     'height': 1.73,
#     'address': [
#         {'street': 'Street Name', 'number': 999},
#         {'other_street': 'Other Street Name', 'other_number': 111},
#     ],
# }
# person = dict(name='Wesley', last_name='Boaes')

person = {
    'name': 'Wesley',
    'last_name': 'Boaes',
    'age': 34,
    'height': 1.73,
    'address': [
        {'street': 'Street Name', 'number': 999},
        {'other_street': 'Other Street Name', 'other_number': 111},
    ],
}
# print(person, type(person))
print(person['name'])
print(person['last_name'])
print('\n#################\n')

for key in person:
    print(key, person[key])

print('\n#################\n')

key = 'name'
person[key] = 'Maiara Boaes'
person['last_name'] = 'Oliveira'

print(person[key])

del person['last_name']
print(person)

# print(person.get('last_name', None))

if person.get('last_name') is None:
    print("DOESN'T EXIST")
else:
    print(person['last_name'])