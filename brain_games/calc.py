from random import randint
from random import choice
import prompt


def game_logic():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')

    i = 0

    while i <= 2:
        a = randint(20, 40)
        b = choice('+-*')
        c = randint(1, 20)
        print(f'Question: {a} {b} {c}')
        answer = prompt.string('Your answer: ')
        tru = ' '
        if b == '+' and answer != str(a + c):
            tru = str(a + c)
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{tru}'.")
            print(f"Let's try again, {name}!")
            break
        elif b == '-' and answer != str(a - c):
            tru = str(a - c)
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{tru}'.")
            print(f"Let's try again, {name}!")
            break
        elif b == '*' and answer != str(a * c):
            tru = str(a * c)
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{tru}'.")
            print(f"Let's try again, {name}!")
            break
        else:
            print('Correct!')
        i += 1
        if i > 2:
            print(f'Congratulations, {name}!')
