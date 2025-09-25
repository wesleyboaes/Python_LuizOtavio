"""
Lists in Python
Type list - Changeable
Supports several values of any type
Reusable knowledge  - indexes and slicing
Usable methods: append, insert, pop, del, clear, extend, +
Create Read Update Delete = list[i] (CRUD)
"""

lists = [10, 20, 30, 40]
# Create
lists.append(50) # Add at the end
print(lists)
# Read
number = lists[0]
print(lists[1:4])
print(number)
# Update
lists[0] = 100
print(lists)
# Delete
del lists[-1]
print(lists)

lists_2 = [1, 2, 3, 4]
lists_2.append(5)
print(lists_2)
lists_2.pop() # Remove the last one
lists_2.append(6)
print(lists_2)
lists_2.append(7)
lists_2.append(8)
removed = lists_2.pop()
print(lists_2, 'Removed:', removed)
lists_2.pop(0)
print(lists_2)