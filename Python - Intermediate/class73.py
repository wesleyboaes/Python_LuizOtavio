"""
Higher Order Functions - Functions that can receive and/or return other functions
First class functions - Functions that are treated as other common data types (strings, integers, etc)
"""
def greeting(msg, name):
    return f'{msg}, {name}!'

def execute(function, *args): # Here *args will pack
    return function(*args) # Here *args will unpack

print(
    execute(greeting, 'Good morning', 'Wesley')
)
print(
    execute(greeting, 'Good afternoon', 'Maiara')
)
print(
    execute(greeting, 'Good evening', 'Sophia')
)
