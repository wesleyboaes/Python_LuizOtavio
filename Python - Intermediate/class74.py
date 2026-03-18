"""
Closure and functions that returns other functions
"""

def create_greeting(greeting):
    def greet(name):
        return f'{greeting}, {name}!'
    return greet

s1 = create_greeting('Good morning')
s2 = create_greeting('Good evening')

print(s1('Wesley'))
print(s2('Wesley'))