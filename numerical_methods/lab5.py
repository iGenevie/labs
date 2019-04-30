from numpy import linspace
from math import log


def arr_print(ch, arr):
    print(ch, end=' | ')
    for num in arr:
        print(f'{num:5.2f}', end=' | ')
    print()


def rect(xs, h, f):
    lmr = [0, 0, 0]

    n = len(xs)

    for i in range(n):
        if i < n - 1:
            lmr[0] += f(xs[i])  # L rect
            lmr[1] += f(xs[i] + h / 2)  # M rect
        if i > 0:
            lmr[2] += f(xs[i])  # R rect

    return (i * h for i in lmr)


def trapeze(xs, h, f):
    res = 0

    for i in range(len(xs) - 1):
        res += f(xs[i]) + f(xs[i + 1])

    return res * h / 2


def parab(xs, h, f):
    res = f(xs[0]) + f(xs[-1])

    res += sum(4 * f(i) for i in xs[1:-1:2])
    res += sum(2 * f(i) for i in xs[2:-2:2])

    return res * h / 3


def gauss_val_init(a, b):
    def gauss_val(x):
        x = (b - a) * x / 2 + (a + b) / 2
        val = x / (x + 3) ** 2

        return val
    return gauss_val


def gauss(a, b):
    x1 = -0.93246951
    x2 = -0.66120939
    x3 = -0.23861919
    x4 = -x3
    x5 = -x2
    x6 = -x4

    x = (x1, x2, x3, x4, x5, x6)

    c1 = c6 = 0.17132449
    c2 = c5 = 0.3606157
    c3 = c4 = 0.46791393

    c = (c1, c2, c3, c4, c5, c6)

    res = 0

    gauss_val = gauss_val_init(a, b)

    for i in range(len(x)):
        res += c[i] * gauss_val(x[i])

    return res * (b - a) / 2


def main():
    a, b, h = 0, 2, 0.2
    n = (b - a) / h + 1

    xs = linspace(a, b, n)

    f = lambda x: x / (x + 3) ** 2
    F = lambda x: 3 / (x + 3) + log(x + 3)

    methods = (
        rect(xs, h, f),
        trapeze(xs, h, f),
        parab(xs, h, f),
        gauss(a, b),
    )

    arr_print('X', xs)
    arr_print('Y', (f(x) for x in xs))

    print(f'F: {F(b) - F(a):.5f}')

    for ch, res in zip('LMR', methods[0]):
        print(f'{ch}: {res:.5f}')

    for l, res in zip(('Trapeze', 'Parab', 'Gauss'), methods[1:]):
        print(f'{l}: {res:.5f}')


if __name__ == '__main__':
    main()
