from random import randint
import prompt


def game_logic():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')

    i = 0

    while i <= 2:
        a = randint(1, 100)
        b = randint(1, 100)
        print(f'Question: {a} {b}')
        answer = prompt.string('Your answer: ')
        tru = ''
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        tru += str(a + b)
        if answer == tru:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{tru}'.")
            print(f"Let's try again, {name}!")
            break
        i += 1
        if i > 2:
            print(f'Congratulations, {name}!')
