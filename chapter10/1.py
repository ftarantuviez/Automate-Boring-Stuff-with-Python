"""Debugging Coin Toss

The following program is meant to be a simple coin toss guessing game. The
player gets two guesses (it’s an easy game). However, the program has several bugs in it. Run through the program a few times to find the bugs that
keep the program from working correctly.

"""

import random, sys


def coin_toss():
    options = ['heads', 'tails']
    while True:

        machine_select = options[random.randint(0, 1)]
        user_select = input('[H] to heads, [T] to tails, [E] to exit: ')
        print('*' * 100)
        
        if user_select.upper() == 'H':
            user_select = 'heads'
        elif user_select.upper() == 'T':
            user_select = 'tails'
        elif user_select.upper() == 'E':
            sys.exit()
        else:
            print('Put a valid command')
            continue

        if user_select == machine_select:
            print('You win, the coin was ' + user_select)
            break
        else:
            print('You lost, try again :(')
            continue

    return



if __name__ == '__main__':

    coin_toss()


