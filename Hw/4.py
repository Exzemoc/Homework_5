from datetime import datetime
from functools import reduce

c: int = 5
b: int = 8
tup = ('цыц', 'кек', 'дааа', 'lool')


def decor(func):
    def dec():
        start = datetime.now()
        func()
        end = datetime.now()
        print(f'Work time = {end - start}')

    return dec


@decor
def pr():
    global c
    print(c)


@decor
def plus():
    global c, b
    print(c + b)


pr()
plus()
