"""
Strings basic interpolation
s - String
d and i - Integer
f - Float
x and X - Hexadecimal (ABCDEF0123456789)
"""

name = 'Wesley'
price = 1000.95897643
variable = '%s, the price is R$ %.2f reais.' % (name, price)
print(variable)

integer = 1500
print('The hexadecimal of %d is %08X.' % (integer, integer))