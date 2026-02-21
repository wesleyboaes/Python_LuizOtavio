"""
Exercise
Ask to the user to type their name
Ask to the user to type their age
If name and age were typed:
    Print:
        Your name is {name}
        Your inverted name is {inverted name}
        If name has (or not) spaces
        If name has {n} letters
        The first letter of your name is {letter}
        The last letter of your name is {letter}
If anything was typed in name or age:
    Print: "Sorry, you left empty fields"
"""

name = input('Enter with your name: ')
age = input('Enter with your age: ')

#if name == '' or age == '':
#     print('Sorry, you left empty fields.')
    
# else:
#     print(f'Your name is {name}')
#     print(f'Your inverted name is {name[::-1]}')
    
#     print(f'Your name has {len(name)} letters')
#     print(f'The first letter of your name is {name[:1]}')
#     print(f'The last letter of your name is {name[len(name)-1:len(name)]}')

if name and age:
    print(f'Your name is {name}')
    print(f'Your inverted name is {name[::-1]}')
    if ' ' in name:
        print(f'{name} has empty fields.')
    else:
        print(f'{name} does not have empty fields')
    print(f'Your name has {len(name)} letters')
    print(f'The first letter of your name is {name[0]}')
    print(f'The last letter of your name is {name[-1]}')
else:
    print('Sorry, you left empty fields.')