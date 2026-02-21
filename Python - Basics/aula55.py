"""
Float point imprecision
Double-precision floating-precision format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/3/tutorial/floatingpoint.html
"""
import decimal

number_1 = decimal.Decimal('0.1')
number_2 = decimal.Decimal('0.7')
number_3 = number_1 + number_2
print(number_3)
print(f'{number_3:.2f}')
print(round(number_3, 10))