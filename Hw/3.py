tup = ('цыц', 'кек', 'дааа', 'lool')


def poli2(l):
    result = filter(lambda x: x == x[::-1], l)
    print(list(result))


poli2(tup)
