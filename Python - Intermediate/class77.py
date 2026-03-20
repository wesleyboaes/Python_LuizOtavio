# Exercise - Questions and answers system

questions = [
    {
        'Question': 'How much is 2 + 2?',
        'Options': ['1', '3', '4', '5'],
        'Answer': '4',
    },
    {
        'Question': 'How much is 5 * 5?',
        'Options': ['25', '55', '10', '51'],
        'Answer': '25',
    },
    {
        'Question': 'How much is 10 / 2?',
        'Options': ['4', '5', '2', '1'],
        'Answer': '5',
    },
]

qnt_correct = 0

for question in questions:
    print('Question:', question['Question'])
    print('Options:\n')

    for i, option in enumerate(question['Options']):
        print(f'{i})', option)
    print()

    choice = input('Choice an answer: ')

    choice_int = None
    qnt_options = len(question['Options'])
    correct = False

    if choice.isdigit():
        choice_int = int(choice)

    if choice_int is not None:
        if choice_int >= 0 and choice_int < qnt_options:
            if question['Options'][choice_int] == question['Answer']:
                correct = True
    
    print()
    if correct:
        print('Got it 👍\n')
        qnt_correct += 1
    else:
        print('Wrong answer ❌\n')

print(f'You answered {qnt_correct} questions of {len(questions)} correctly')