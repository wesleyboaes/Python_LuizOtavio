"""
Lists in Python
Type list - Changeable
Supports several values of any type
Reusable knowledge  - indexes and slicing
Usable methods: append, insert, pop, del, clear, extend, +
Create Read Update Delete = list[i] (CRUD)
"""


#        +01234
#        -54321
string = 'ABCDE' # 5 characters (len)
list_1 = [] # or list() # '' (empty)
print(list_1, type(list_1))
print(bool(list_1)) # falsy, because it is empty


#          0 ,  1  ,     2   ,  3 ,  4
#         -5 ,  -4  ,   -3   , -2 , -1
list_2 = [123, True, 'Wesley', 1.2, []]
print(list_2)
print(list_2[2])
list_2[2] = 'Boaes'
print(list_2[-3], type(list_2[2]))

