phrase = 'Python is a program language '\
    'multiparadigm. '\
    'Python was created by Guido Van Rossum.'.lower() # Keep everything lower case 

# Index
i = 0

# The letter that appears most often
more_times_letter = ''

# Count the letter that appears most often 
quantity_more_times_letter = 0

while i < len(phrase):
    actual_letter = phrase[i]

    # How many times the letter appears
    quantity_actual_letter= phrase.count(actual_letter)

    # jump repeated letters
    if actual_letter in phrase[:i]: 
        i += 1
        continue

    # jump spaces and dots
    if actual_letter == ' ' or actual_letter == '.':
        i += 1
        continue

    # If the letter that appear most frequently is smaller, it receives the value of the current letter. Because if it is smaller, the current one is the letter that appears most frequently.
    if quantity_more_times_letter < quantity_actual_letter:
        # The letter that appears most frequently receives the value of the current one (Because the current one is greater than the most frequent one)
        quantity_more_times_letter = quantity_actual_letter
        # The letter changes too, because it is the most frequent letter
        more_times_letter = actual_letter

    i += 1

print(f'The letter that appeared most frequently was {more_times_letter}. It appeared {quantity_more_times_letter} times.')
