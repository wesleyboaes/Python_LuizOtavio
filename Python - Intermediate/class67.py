"""
Default values for parameters
When defining a function, parameters can have default values.
If no values is provided for the parameter, the default value will be used.
Refactor: Edit your code.
"""

def soma(x, y, z = None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)

soma (1, 2)
soma (7, 9, 0)