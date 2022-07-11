from random import randint
import prompt


def game_logic():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
  
    i = 0
  
    while i <= 2:
      question = []
      list_of_ints = list(range(randint(1, 5), 60, randint(1, 5)))
      random_n = randint(0, 9)
      for x in list_of_ints:
        question += [x]
        if len(question) > 10:
          q = question[:random_n] + ['..'] + question[random_n+1:10]
  
      print(f"Question: {' '.join(map(str, q))}")
      correct_answer = question[random_n]
      answer = prompt.string('Your answer: ')
      if str(correct_answer) == answer:
        print('Correct!')
      else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}!")
        break
      i += 1
      if i > 2:
        print(f'Congratulations, {name}!')