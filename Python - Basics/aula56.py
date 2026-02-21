"""
split and join with list and str
split - splits a string (list)
join - joins a string (strings, lists and tuples)
"""
phrase = '    Look, what an interesting thing!'
word_list = phrase.split() # The default is to split on empty spaces
print(word_list)

word_list = phrase.split('a')
print(word_list)

without_spaces = []
word_list = phrase.split(',')
for i, phrase in enumerate(word_list):
    print(word_list[i].strip()) # Removes empty spaces at the beginning and end. 'rstrip' for the right and 'lstrip' for the left.
    without_spaces.append(word_list[i].strip()) # I use append to insert the value without spaces in my variable 'without_spaces'

print(word_list)
print(without_spaces)

joined_phrases = '-'.join('abc')
print(joined_phrases)

joined_phrases = '-,+='.join(without_spaces)
print(joined_phrases)

joined_phrases = ', '.join(without_spaces)
print(joined_phrases)