"""
Layered unpacking
Methods and functions
"""
string = 'ABCD'
lists = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tuples = 'Python', 'is', 'nice'

rooms = [
    # 0        1
    ['Maria', 'Helena', ],  # Index 0
    # 0
    ['Elaine', ],  # Index 1
    # 0       1      2
    ['Luiz', 'João', 'Eduarda',] # (0, 10, 20, 30, 40)]  # Index 2
]

first, second, *_, penultimate, last = lists # '*_' Is what remains from my list
print(first, last)

for name in lists:
    print(name, end = ' ') # Unpacking

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

print(*lists)
print(*string)
print(*tuples)

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

print(*rooms, sep = '\n')