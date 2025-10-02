"""
Introducing to unpacking and tuples
"""

# names = ['Wesley', 'Pimenta', 'Boaes']

# name1, name2, name3 = names

name1, name2, name3 = ['Wesley', 'Pimenta', 'Boaes'] # Must have the same size

print(name1)

# If I want to use just on or two values of my list, I need to pack the others 

_, _, name3, *remainder = ['Wesley', 'Pimenta', 'Boaes']

print(name1, remainder)