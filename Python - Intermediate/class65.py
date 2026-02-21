"""
Introduction to functions (def) in Python.
Functions are sections of code used to replicate a specific action throughout your code.
They can receive values for parameters (arguments) and return a specific value.
By default, Python functions returns "None".
"""

def imprimir(a, b, c):
    print(a, b, c)

imprimir(1, 2, 3)

def greeting(name='John Doe'):
    print(f'Hello {name}!')

greeting('Wesley')
greeting()