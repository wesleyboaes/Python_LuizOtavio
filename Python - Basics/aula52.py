"""
Type tuple - immutable list
"""

names = 'Wesley', 'Pimenta', 'Boaes'
print(names[-1])
print(names)

names1 = ('Wesley', 'Pimenta', 'Boaes') # It can be like this
print(names1)

names2 = ['Wesley', 'Pimenta', 'Boaes']
print(names2)
names3 = tuple(names2) # You can convert list to tuple
print(names3)
names2 = list(names3) # And convert tuple to list too
print(names2)