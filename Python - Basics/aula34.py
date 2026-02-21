"""
Repetitions 
while
Execute an action while a condition is true
Infinite loop -> When a code does not end
"""

condition = True

while condition:
    name = input('What is your name: ')
    print(f'Your name is {name}')

    if name == 'End':
        break

print('It is over!')