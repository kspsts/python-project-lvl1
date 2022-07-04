#!/usr/bin/env python
from unicodedata import name
from brain_games.cli import welcome_user


def main():
    print('Welcome to the Brain Games!')
    user_name = welcome_user()


if __name__ == '__main__':
    main()
