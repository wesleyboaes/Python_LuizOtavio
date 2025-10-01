"""
Calculating the first digit of a CPF
CPF: 746.824.890-70
Collect the sum of the first 9 digits of CPF multiplying each value by a countdown starting with 10

E.g. 746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*   7  4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Sum all the results:
70 + 36 + 48 + 56 + 12 + 20 + 32 + 27 + 0 = 301
Multiply the last result by 10
301 * 10 = 3010
Get the rest of division on last account by 11
3010 % 11 = 7
If the result is greater than 9:
    result is 0
else:
   result is the value of account

The first digit of CPF is 7
"""

cpf = '746.824.890-70'

print(f'The cpf is {cpf}')

split_digit = cpf.split('-')

split_numbers = split_digit[0].split('.')

list_main_numbers = list(''.join(split_numbers))
# print(list_main_numbers)

counter_first_digit = 10
result_first_digit = 0
for i, number in enumerate(list_main_numbers):
   result_first_digit += int(number) * counter_first_digit
   counter_first_digit -= 1

cpf_first_digit = (result_first_digit * 10) % 11
cpf_first_digit = cpf_first_digit if cpf_first_digit <= 9 else 0

print(f'The first digit of CPF is {cpf_first_digit}')