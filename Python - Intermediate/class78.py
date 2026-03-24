# Sets - Conjuntos em Python
# Sets are taught in math
# Graphically represented by Venn diagram
# Sets in Python are immutable, nut they only accept immutable types as their internal value

# Creating a set
# set(iterable) or {1, 2, 3}

# s1 = set() # empty
# s2 = {'Wesley', 1, 2, 3} # with data
# print(s1)
# print(s2)

# Sets are efficient for removing duplicate values from iterable
# - they don't have indexes;
# - they don'n guarantee order
# - they are iterable (for, in, not in)

# l1 = [1, 2, 3, 3, 3, 3, 3, 1]
# s1 = set(l1)
# l2 = list(s1)
# s1 = {1, 2, 3}
# print(3 not in s1)
# for _ in s1:
#     print(_)

# Useful methods:
# add, update, clear, discard

# s1 = set()
# s1.add('Wesley')
# s1.add(1)
# s1.update(('Hello World', 1, 2, 3, 4))
# # s1.clear()
# s1.discard('Hello World')
# s1.discard('Wesley')
# print(s1)

# Useful operators:
# union | - join
# intersection & - items in both
# difference - - items present only in the set on the left
# symmetric difference ^ - items not present in both

s1 = {1, 2, 3}
s2 = {3, 2, 3, 4}
s3 = s1 | s2
s4 = s1 & s2
s5 = s1 - s2
s6 = s1 ^ s2
print(s3)
print(s4)
print(s5)
print(s6)