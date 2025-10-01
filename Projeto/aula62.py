"""
Calculating the second digit of a CPF
CPF: 746.824.890-70
Collect the sum of the first 9 digits of CPF plus the first digit, multiplying each value by a countdown starting with 11

E.g. 746.824.890-70 (746824890)
   11 10  9  8  7  6  5  4  3  2
*   7  4  6  8  2  4  8  9  0  7 <-- FIRST DIGIT
   77 40 54 64 14 24 40 36  0 14

Sum all the results:
77 + 40 + 54 + 64 + 14 + 24 + 40 + 36 + 0 + 14 = 363
Multiply the last result by 10
363 * 10 = 3630
Get the rest of division on last account by 11
3630 % 11 = 0
If the result is greater than 9:
    result is 0
else:
   result is the value of account

The second digit of CPF is 0
"""

cpf = '746.824.890-70'
cpf = '145.925.447-30'

print(f'The cpf is {cpf}')

split_digit = cpf.split('-')

split_numbers = split_digit[0].split('.')

list_main_numbers_first = list(''.join(split_numbers))
# print(list_main_numbers_first)

counter_first_digit = 10
result_first_digit = 0
for i, number in enumerate(list_main_numbers_first):
   result_first_digit += int(number) * counter_first_digit
   counter_first_digit -= 1

cpf_first_digit = (result_first_digit * 10) % 11
cpf_first_digit = cpf_first_digit if cpf_first_digit <= 9 else 0

print(f'The first digit of CPF is {cpf_first_digit}')

cpf_first_digit_str = str(cpf_first_digit)

list_main_numbers_second = list_main_numbers_first.copy()
list_main_numbers_second.append(cpf_first_digit_str)

counter_second_digit = 11
result_second_digit = 0
for i, number in enumerate(list_main_numbers_second):
   result_second_digit += int(number) * counter_second_digit
   counter_second_digit -= 1

cpf_second_digit = (result_second_digit * 10) % 11
cpf_second_digit = cpf_second_digit if cpf_second_digit <= 9 else 0

print(f'The second digit of CPF is {cpf_second_digit}')

new_cpf = split_digit[0] + '-' + str(cpf_first_digit) + str(cpf_second_digit)
# print(new_cpf)
valid_cpf = f'The cpf {cpf} is valid!' if cpf == new_cpf else f'The cpf {cpf} is not valid!'
print(valid_cpf)