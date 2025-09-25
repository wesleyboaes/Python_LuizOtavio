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

lists_a = [1, 2, 3]
lists_b = [4, 5, 6]
lists_c = lists_a + lists_b
print(lists_c)
lists_d = lists_a.extend(lists_b)
print(lists_d) # It returns NONE, because it change the value of lists_a and doesn't return a value to lists_d
print(lists_a) # Here you can see that lists_a changed, so you can't return the value for a variable
lists_a.extend(lists_b) # Here is the correct form, but as I used before, now it has extended twice
print(lists_a)