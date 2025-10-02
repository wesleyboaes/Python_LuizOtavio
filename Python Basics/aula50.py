"""
Exercise
Show list indexes
"""

lista = ['Wesley', 'Pimenta', 'Boaes']

print(lista)

for name in lista:
    print(f'Index of {name} is: {lista.index(name)}')

# Other mode

indexes = range(len(lista))
print(indexes)

for index in indexes:
    print(index, lista[index], type(lista[index]))