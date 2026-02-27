"""
Functions scope in Python
Scope refers to the area where that code can reach.
There is global scope and local one.
Global scope is the area where all the code is reachable.
Local scope is the area where only names from the same location can be reached.
"""

x = 1

def scope():
    global x
    x = 10

    def other_function():
        x = 11
        y = 2
        print(x, y)
    
    other_function()
    print(x)

print(x)
scope()
print(x) # Because of the global x, the variable is changed after the function scope()
