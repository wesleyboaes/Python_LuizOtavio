"""
enumerate - enumerates iterables (indexes)
"""

lista = ['Wesley', 'Pimenta', 'Boaes']
lista_enumerated = enumerate(lista)

print(lista_enumerated) # Shows the memory local because it is an iterator

print('###########################')

# So, we use FOR to loop through the entire list

for items in lista_enumerated:
    print(items)

lista_enumerated_2 = list(enumerate(lista))
print(lista_enumerated_2)

print('###########################')

# We can unpack the tuples, so we can do like this:
for item in enumerate(lista):
    index, name = item
    print(index, name)

print('###########################')
# To make it even simpler...
for index, name in enumerate(lista):
    print(index, name)