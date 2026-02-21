"""
Creating new CPFs
"""
import random

nine_digits = ''

for i in range(0,9):
   nine_digits += str(random.randint(0,9))

print(nine_digits)

counter_first_digit = 10
result_first_digit = 0
for number in nine_digits:
   result_first_digit += int(number) * counter_first_digit
   counter_first_digit -= 1

cpf_first_digit = (result_first_digit * 10) % 11
cpf_first_digit = cpf_first_digit if cpf_first_digit <= 9 else 0

print(f'The first digit of CPF is {cpf_first_digit}')

cpf_first_digit_str = str(cpf_first_digit)
cpf_with_one_digit = nine_digits + cpf_first_digit_str

counter_second_digit = 11
result_second_digit = 0
for number in cpf_with_one_digit:
   result_second_digit += int(number) * counter_second_digit
   counter_second_digit -= 1

cpf_second_digit = (result_second_digit * 10) % 11
cpf_second_digit = cpf_second_digit if cpf_second_digit <= 9 else 0

print(f'The second digit of CPF is {cpf_second_digit}')

new_cpf = f'{nine_digits}{cpf_first_digit}{cpf_second_digit}'
print(f'The cpf is: {new_cpf[:3]}.{new_cpf[3:6]}.{new_cpf[6:9]}-{new_cpf[9:]}')