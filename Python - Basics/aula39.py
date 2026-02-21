"""
Interacting strings with while
"""

name = input('Enter your name: ')
name_size = len(name)

index = 0

# while index < name_size:
    
#     print(name[letter])

#     index += 1

new_name = ''

while index < name_size:
    letter = name[index]
    new_name += f'*{letter}' #new_name = new_name + f'*{letter}'
    index += 1

print(new_name + '*')