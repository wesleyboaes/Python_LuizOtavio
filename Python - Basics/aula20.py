first_value = input('Type a value: ')
second_value = input('Type another value: ')

if first_value > second_value:
    print(f'{first_value=} is greater than {second_value=}')

elif first_value < second_value:
    print(f'{second_value=} is greater than {first_value=}')

else:
    print(f'{first_value=} is equal to {second_value=}')