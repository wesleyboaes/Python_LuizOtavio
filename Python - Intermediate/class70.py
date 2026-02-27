"""
Return values from the functions (return)
"""

variavel = print('Hello World!')
print(variavel)
print(variavel is None)

def soma (x, y):
    # x + y # The exit is None
    return x + y # The exit is Literal

soma1 = soma(1, 2)
soma2 = soma(3, 3)
print(soma1 + soma2)
