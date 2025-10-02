"""
Iterable -> str, range, etc (__iter__)
Iterator -> Who knows to deliver one value at a time
next -> give me the next value
iter -> give me the iterator
"""
text = 'Wesley'.__iter__() # Shows the iterator of the string at the memory location
text_2 = iter('Wesley') # The function to show the iterator.

print(text)
print(text_2.__next__())
print(text_2.__next__())
print(text_2.__next__())
print(next(text_2))
print(next(text_2))
print(next(text_2))
print('\n')

###########################

# for letter in new_text
new_text = 'Boaes' # Iterable
iterator = iter(new_text) # Iterator

while True:
    try:
        letter = next(iterator)
        print(letter)
    except StopIteration:
        break

###########################

print('\n')
for letter in new_text:
    print(letter)