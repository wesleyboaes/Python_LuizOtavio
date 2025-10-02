"""
List of lists and their indexes
"""

rooms = [
    # 0        1
    ['Maria', 'Helena', ],  # Index 0
    # 0
    ['Elaine', ],  # Index 1
    # 0       1      2
    ['Luiz', 'João', 'Eduarda',] # (0, 10, 20, 30, 40)]  # Index 2
]

print(rooms)

print(rooms[0][1]) # The first brackets are the main list index, the second ones are the inner list
print(rooms[2][1])
# print(rooms[2][3][4])

for room in rooms:
    print(room)
    for student in room:
        print(student)