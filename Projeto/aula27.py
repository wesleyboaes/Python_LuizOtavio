"""
Strings slicing
012345678
Hello World
-987654321
Slicing [i:f:p] [::]
Obs: The len function returns the length of the string (the number of characters)
"""

variable = 'Hello World'
print(variable[8])
print(variable[-3])
print(variable[6:])
print(variable[6:9])
print(variable[:5])
print(variable[-11:-6])
print(len(variable[-11:-6]))
print(len(variable))
print(variable[0:len(variable):2])
print(variable[::-1])
print(variable[-1:-12:-1])