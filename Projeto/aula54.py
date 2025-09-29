"""
Create a shopping list with lists.
The user should be able to insert, delete and list values in the list.
Avoid allowing the program to crash with non-existent index errors.
"""

import os

lista = [] # Empty list

while True:
    print('Select an option:')
    option = input('[i]nsert [d]elete [l]ist: ')

    if option == 'i':
        os.system('cls' if os.name == 'nt' else 'clear') # Clear terminal
        item = input('Item: ')
        lista.append(item)
    
    elif option == 'd':
        delete_str = input('Chose the index to delete: ')

        try:
            delete_int = int(delete_str) # Converts to integer
            del lista[delete_int] # Deletes the chosen index
        except:
            print('It is not possible to delete this index!')
    
    elif option == 'l':
        os.system('cls' if os.name == 'nt' else 'clear') # Clear terminal
        if len(lista) < 1:
            print('Nothing to list!')
        else:
            for index, name in enumerate(lista):
                print(f'{index}.', name)

    elif option == 'exit':
        break

    else:
        print('Please, chose [i] [d] or [l]"')
        continue