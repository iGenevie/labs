from math import (
    log,
    ceil,
    fabs,
)

import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return log(x) + (x + 1) ** 3


def arr_print(ch, nums):
    print(ch, end=' | ')
    for num in nums:
        print(f'{num:5.2f}', end=' | ')
    print()


def calc_fi(i, h, ys):
    return (6 / h ** 2) * (ys[i + 1] - 2 * ys[i] + ys[i - 1])


def spline_coef(ys, n, h):
    arr = [[] for i in range(4)]
    arr[0] = ys
    arr[1].append(0)

    seq = [0, 1]
    seq.extend(4 * seq[i - 1] - seq[i - 2] for i in range(2, n))

    arr[2].append(0)
    for i in reversed(range(2, n)):
        slag = 0
        minus = 1
        for j in reversed(range(1, i)):
            slag += minus * seq[j] * calc_fi(j, h, ys)
            minus *= 1
        slag = (slag - arr[2][0] * seq[i - 1]) / seq[i]
        arr[2].append(slag)
    arr[2].append(0)
    arr[2].reverse()

    arr[3].append(0)
    for i in range(1, n):
        arr[3].append(
            (arr[2][i] - arr[2][i - 1]) / h
        )
        arr[1].append(
            (arr[2][i] * h / 2) -
            (arr[3][i] * (h ** 2) / 6) +
            (arr[0][i] - arr[0][i - 1]) / h
        )

    return arr


def s(x, xs, c, n, h):
    num = 0
    for i in range(n):
        if ceil(fabs(xs[i] - x) / h) < 2:
            num = i + 1
            break

    return c[0][num] + \
           c[1][num] * (x - xs[num]) + \
           c[2][num] * ((x - xs[num]) ** 2) / 2 + \
           c[3][num] * ((x - xs[num]) ** 3) / 6


def main():
    # Исходные данные
    a, b, h, n = 1, 2, 0.2, 6

    xs_check = (
        a + 0.5 * h,
        0.5 * a + 0.5 * b,
        b - 0.5 * h
    )

    # Инициализация xs, вычисляем ys
    xs = np.linspace(a, b, n)
    ys = tuple(f(x) for x in xs)

    func_str = 'ln(x) + (x + 1)^3'
    print(f'f(x) = {func_str}\n')

    arr_print("X", xs)
    arr_print("Y", ys)

    c = spline_coef(ys, n, h)

    for x in xs_check:
        print(x, f(x), s(x, xs, c, n, h))

    for i in range(n - 1):
        a_i, b_i = i, i + 2
        xs_range = xs[a_i:b_i]

        plt.plot(
            xs, ys, "x",
            xs, ys,
            xs_range, [s(x, xs, c, n, h) for x in xs_range], "b"
        )

        plt.legend([f'Отрезок [X{i}; X{i + 1}]', func_str, 'Кубический сплайн'])
        plt.title("Интерполяция кубическими сплайнами")
        plt.show()


if __name__ == '__main__':
    main()
