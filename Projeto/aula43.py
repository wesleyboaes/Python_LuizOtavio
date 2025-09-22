text = 'Python'

new_text = ''

for letter in text:
    print(letter)
    new_text += f'*{letter}'

print(new_text + '*')