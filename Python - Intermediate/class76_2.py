# Keys and values manipulation in dictionaries

person = {}

key = 'name'

person[key] = 'Wesley'
person['last_name'] = 'Boaes'

print(person[key])

person[key] = 'Maiara'

del person['last_name']
print(person)
print(person['name'])

# print(person.get('last_name', None))

if person.get('last_name') is None:
    print("DOESN'T EXIST")
else:
    print(person['last_name'])