import math


def egyptian_fraction(nr, dr):
    dems = []
    while nr > 0:
        x = math.ceil(dr/nr)
        dems.append(x)
        nr = x * nr - dr
        dr = dr * x
    return '+'.join(['1/{}'.format(d) for d in dems])


if __name__ == '__main__':
    print(egyptian_fraction(2, 3))
    print(egyptian_fraction(6, 14))