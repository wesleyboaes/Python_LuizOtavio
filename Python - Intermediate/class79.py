# Example of using sets

letters = set()
while True:
    letter = input('Type a letter: ')
    letters.add(letter.lower())

    if 'w' in letters:
        print('Congrats!')
        break

    print(letters)