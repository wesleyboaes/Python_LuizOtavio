"""
Ternary operation, one-line condition
<value> if <condition> else <other value>
"""

print('Value' if True else 'Other value')
print('Value' if False else 'Other value')

print('Value' if False else 'Other value' if False else 'End')