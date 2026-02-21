"""
Introducing try/except
try -> attempt to run the code
except -> an error occurred while attempting to run the code
"""
number_str = input('I will double the number you enter: ')

try:
    number_float = float(number_str)
    print('FLOAT: ', number_float)
    print(f'The double of {number_str} is {number_float * 2:.2f}')
except:
    print('This is not a number!')