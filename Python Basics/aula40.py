"""
Calculator with while
"""

while True:
    
    num_1 = input('Enter the first number: ')
    num_2 = input('Enter the second number: ')
    op = input('Enter one of the operators ([+] [-] [*] [/]): ')

    valid_numbers = None
    
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        valid_numbers = True
    except:
        valid_numbers = None

    if valid_numbers is None:
        print('One or more numbers are not valid!')
        continue

    operator = '+-*/'

    if op not in operator:
        print('Operator is not valid!')
        continue

    if len(op) > 1:
        print('Enter just one operator!')
        continue

    if op == '+':
        result = num_1_float + num_2_float
    
    elif op == '-':
        result = num_1_float - num_2_float

    elif op == '*':
        result = num_1_float * num_2_float

    elif op == '/':
        if num_2_float == 0:
            
            print('Denominator can not be zero!')
            
            while num_2_float == 0:
                num_2_float = float(input('Enter another denominator: '))

            result = num_1_float/ num_2_float

        else:
            result = num_1_float / num_2_float
    
    print(f'The result is {result:.2f}')

    # Finishing the program

    quit = input('Do you want to [q]uit? ').lower().startswith('q')
    # quit = input('Do you want to [q]uit? ')
    # quit = quit.lower().startswith('q')

    # print(quit)
    
    if quit:
        break