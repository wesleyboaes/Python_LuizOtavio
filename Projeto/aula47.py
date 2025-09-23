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
        correct_letters += letter_typed

    new_word = ''

    for secret_letter in secret_word:
        if secret_letter in correct_letters:
            new_word += secret_letter
        else:
            new_word += '*'

    print(f'The word formed is: {new_word}')

    if new_word == secret_word:
        os.system('cls' if os.name == 'nt' else 'clear')
        # subprocess.run('cls', shell=True)
        print('Congratulations! You got it right!')
        print('The secret word is:', secret_word)
        print(f'Number of attempts: {attempts}')
        correct_letters = ''
        attempts = 0
        break
    else:
        continue