"""
Named and unnamed arguments in Python functions
Named arguments have their name followed by an equal sign
Unnamed arguments receive only the argument (value)
"""

def soma(x, y):
    # definition
    print(f'{x=} + y={y}', '|', 'x + y = ', x + y)

print(soma) # Prints what is the function and where is it
print(soma(1, 2)) # Prints the result and the type of the result

soma(1, 2) # Executes the function
soma(y=2, x=1)
