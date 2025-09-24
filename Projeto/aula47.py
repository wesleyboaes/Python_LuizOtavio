"""
Create a game to the user guess the secret word.
- You will propose any secret world and give the possibility to the user type just one letter.
- When the user type a letter, you check if it is on the secret word.
    - If the letter is on the secret word; show the letter
    - If it is not; show *.
Count the user attempts.
"""

import os
# import sys, subprocess

secret_word = 'python'
correct_letters = ''
attempts = 0

while True:

    letter_typed = input('Type a letter: ')
    
    attempts += 1
    
    if len(letter_typed) > 1:
        print('Type just one letter!')
        continue

    if letter_typed in secret_word:
        correct_letters += letter_typed # Creating a string with correct letters

    new_word = ''

    for letter in secret_word: # Check each secret word index
        if letter in correct_letters: # Check if the letter of that index makes part of the string correct letter
            new_word += letter
        else:
            new_word += '*'

    print(f'The word formed is: {new_word}')

    if new_word == secret_word:
        os.system('cls' if os.name == 'nt' else 'clear')
        # subprocess.run('cls', shell=True)
        print('Congratulations! You got it right!')
        print('The secret word is:', secret_word)
        print(f'Number of attempts: {attempts}')
        again = input('Do you want to go again? [y] or [n]')
        if again == 'y':
            correct_letter = ''
            attempts = 0
            continue
        else:
            break