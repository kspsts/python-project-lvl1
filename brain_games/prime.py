from random import randint
import prompt


def game_logic():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
  
    i = 0
  
    while i <= 2:
      prime_numbers = [2,	3,	5,	7,	11,	13,	17,	19,	23,
29,	31,	37,	41,	43,	47,	53,	59,	61, 67,	71,	73,	79,	83,	89,	97,	101]
      random_numbers = randint(1, 103)
      print(f'Question: {random_numbers}')
      answer = prompt.string('Your answer: ')

      if random_numbers in prime_numbers and answer != 'yes':
        print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'. \nLet's try again, {name}!")
        break
      if random_numbers not in prime_numbers and answer != 'no':
        print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'. \nLet's try again, {name}!")
        break
      else:
        print('Correct!')
        i += 1
      if i > 2:
        print(f'Congratulation, {name}!')