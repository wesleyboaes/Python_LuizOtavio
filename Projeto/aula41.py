""" while/else """

string = 'Anyvalue'

i = 0
letter = ''

while i < len(string):
    letter = string[i]

    if letter == ' ':
        break

    print(letter)

    i += 1
else:
    print('The else was executed')
    print('The string does not have spaces!')

print('Out of while!')