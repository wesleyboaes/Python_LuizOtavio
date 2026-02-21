"""
For + Range
range -> range(start, stop, step)
"""

numbers = range(10)
numbers_2 = range(5, 10)
numbers_3 = range(5, 10, 2)

print(numbers)
print(numbers_2)
print(numbers_3)

print('#########################')

for value in numbers:
    print(value)

print('#########################')

for value in numbers_2:
    print(value)

print('#########################')

for value in numbers_3:
    print(value)