"""
Closure and functions that returns other functions
"""

def create_greeting(greeting, name):
    def greet():
        return f'{greeting}, {name}!'
    return greet

s1 = create_greeting('Good morning', 'Wesley')

print(s1())