"""
Flag - Marks a place
None = No value
is and is not (type, value, identity)
id = identity
"""

# v1 = 'a'
# v2 = 'a'

# print(id(v1))
# print(id(v2))

condition = False
passed_on_if = None

if condition:
    passed_on_if = True
    print('Do something')
else:
    print('Do nothing')

print(passed_on_if, passed_on_if is None)
print(passed_on_if, passed_on_if is not None)