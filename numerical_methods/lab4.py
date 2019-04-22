from math import e
import numpy as np


def arr_print(ch, arr):
    print(ch, end=' | ')
    for num in arr:
        if num is None:
            print(f' {num}', end=' | ')
        else:
            print(f'{num:5.2f}', end=' | ')
    print()


def f(x):
    return e ** x + x ** 2


def deriv(x):
    return e ** x + 2 * x


def deriv_sec(x):
    return e ** x + 2


def deriv_lrm(xs, ys, h):
    res = [[] for i in range(3)]

    res[1].append(None)
    res[2].append(None)

    for i in range(len(xs)):
        if i < len(xs) - 1:
            res[0].append((ys[i + 1] + ys[i]) / h)  # L deriv
        if i > 0:
            res[1].append((ys[i] - ys[i - 1]) / h)  # R deriv
        if 0 < i < len(xs) - 1:
            res[2].append((ys[i + 1] - ys[i - 1]) / h)  # M deriv

    res[0].append(None)
    res[2].append(None)

    return res


def deriv_sec_appr(xs, ys, h):
    res = [None, ]

    for i in range(1, len(xs) - 1):
        res.append((ys[i + 1] - 2 * ys[i] + ys[i - 1]) / h ** 2)

    res.append(None)

    return res


def main():
    # Исходные данные
    a, b, h = -1, 0, 0.2
    n = (b - a) / h + 1

    # Инициализация xs, вычисляем ys
    xs = np.linspace(a, b, n)
    ys = tuple(f(x) for x in xs)

    ys_deriv = (deriv(x) for x in xs)
    ys_deriv_lrm = deriv_lrm(xs, ys, h)

    ys_deriv_sec = (deriv_sec(x) for x in xs)
    ys_deriv_sec_appr = deriv_sec_appr(xs, ys, h)

    arr_print('X', xs)
    arr_print('Y', ys)
    arr_print('1', ys_deriv)

    for ch, l in zip(('L', 'R', 'M'), ys_deriv_lrm):
        arr_print(ch, l)

    arr_print('2', ys_deriv_sec)
    arr_print('A', ys_deriv_sec_appr)


if __name__ == '__main__':
    main()
