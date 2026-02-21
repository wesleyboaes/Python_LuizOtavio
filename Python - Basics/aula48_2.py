"""
Lists in Python
Type list - Changeable
Supports several values of any type
Reusable knowledge  - indexes and slicing
Usable methods: 
    append - Add an item at the end
    insert - Adds an item at the chosen index
    pop - Removes from the end or at the chosen index
    del - Deletes an index
    clear - Clear the list
    extend - Extends the list
    + - Concatenates the list
Create Read Update Delete = list[i] (CRUD)
"""

#        0 , 1 , 2 , 3  
lists = [10, 20, 30, 40]
lists.append('Wesley')
name = lists.pop()
lists.append(1234)
del lists[-1]
# lists.clear()
lists.insert(0, 5) # It takes 2 arguments, first is the index and second is the value.
print(lists)