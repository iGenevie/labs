from numpy import array, linalg
import matplotlib.pyplot as plt


def pow_x(xs, p):
    """Return collection, which contains x ^ p"""
    return (x ** p for x in xs)


def pow_yx(xs, p, ys):
    """Return collection, which contains y * x ^ p"""
    return (x * y for x, y in zip(pow_x(xs, p), ys))


def coef_1(xs, ys):
    a_arr = array(
        (
            tuple(sum(pow_x(xs, i)) for i in (2, 1)),
            tuple(sum(pow_x(xs, i)) for i in (1, 0)),
        )
    )

    b_arr = array(
        tuple(sum(pow_yx(xs, i, ys)) for i in (1, 0)),
    )

    return linalg.solve(a_arr, b_arr)  # x_arr


def coef_2(xs, ys):
    a_arr = array(
        (
            tuple(sum(pow_x(xs, i)) for i in (4, 3, 2)),
            tuple(sum(pow_x(xs, i)) for i in (3, 2, 1)),
            tuple(sum(pow_x(xs, i)) for i in (2, 1, 0)),
        )
    )

    b_arr = array(
        tuple(sum(pow_yx(xs, i, ys)) for i in (2, 1, 0))
    )

    return linalg.solve(a_arr, b_arr)  # x_arr


def coef_3(xs, ys):
    a_arr = array(
        (
            tuple(sum(pow_x(xs, i)) for i in (6, 5, 4, 3)),
            tuple(sum(pow_x(xs, i)) for i in (5, 4, 3, 2)),
            tuple(sum(pow_x(xs, i)) for i in (4, 3, 2, 1)),
            tuple(sum(pow_x(xs, i)) for i in (3, 2, 1, 0)),
        )
    )

    b_arr = array(
        tuple(sum(pow_yx(xs, i, ys)) for i in (3, 2, 1, 0))
    )

    return linalg.solve(a_arr, b_arr)  # x_arr


def func_graph(xs, ys, coef, f):
    plt.plot(
        xs, ys, 'x',
        xs, ys,
        xs, tuple(f(x, *coef) for x in xs), 'b'
    )
    plt.show()


def main():
    xs = tuple(x for x in range(-3, 4))
    ys = (2.6, -0.3, -2, -2.3, -1.5, 0.7, 3.2)

    fs = (
        lambda x, a, b: a * x + b,
        lambda x, a, b, c: a * x ** 2 + b * x + c,
        lambda x, a, b, c, d: a * x ** 3 + b * x ** 2 + c * x + d,
    )

    coef = (coef_1, coef_2, coef_3)

    for _c, f in zip(coef, fs):
        func_graph(xs, ys, _c(xs, ys), f)


if __name__ == "__main__":
    main()
