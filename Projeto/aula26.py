"""
Strings basic formatting
s - String
d - Integer
f - Float
.<number of digits>f - Float with fixed number of digits after the dot
x or X - Hexadecimal
(Character)(><^)(quantity)
> - Left align
< - Right align
^ - Center align
= - Forces the padding to be placed after the signal
Signal - + or -
E.g.: 0>-100,.1f
Conversion flags - !r !s !a
"""

variable = 'Wesley'
print(f'{variable}')
print(f'{variable:#>10}')
print(f'{variable: <10}.')
print(f'{variable:$^10}.')
print(f'{10000.9843251685:0>+15,.2f}')
print(f'{10000.9843251685:0=+15,.2f}')