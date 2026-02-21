# in and not in operators
# Strings are iterable (You can navigate through each character)
# You can use the 'in' operator to check if a substring exists within a string
# 0 1 2 3 4 5
# W e s l e y
# -6-5-4-3-2-1

# name = 'Wesley'
# print(name[1])
# print(name[-4])
# print('Wes' in name)
# print('Boaes' not in name)

name = input('Type your name: ')
find = input('Type what you want to find: ')

if find in name:
    print(f'Found {find} in {name}')

else:
    print(f'Did not find {find} in {name}')