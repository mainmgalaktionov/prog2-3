from random import *


def main():
    rannndom = randint(0, 100)
    x = None
    bolwe = 'число больше '
    menshe = 'число меньше '
    print('Угадайте число: ')
    while x != rannndom:
        x = int(input())
        if x < rannndom:
            print('Не угадал, {}'.format(bolwe))
        elif x > rannndom:
            print('Не угадал, {}'.format(menshe))
        else:
            print('Угадали!')



main()