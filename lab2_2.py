# Метод сопряженных направлений
from sympy import diff, symbols


x1, x2 = 1, 2
eps = 0.001


def func(x1, x2):
    return x1 ** 2 - x1 * x2 + x2 ** 2


def get_t(x1, x2, d):
    d1 = d[0]
    d2 = d[1]
    func = x1 ** 2 - x1 * x2 + x2 ** 2
    #new_func = (x1 + t * d[0]) ** 2 - (x1 + t * d[0]) * (x2 + t * d[1]) + (x1 + t * d[0]) ** 2
    t = symbols('t')
    new_t = diff((x1 + t * d1) ** 2 - (x1 + t * d1) * (x2 + t * d2) + (x1 + t * d1) ** 2, t)
    print(new_t)
    #print((diff(new_func, t)))
    #return new_t


if __name__ == "__main__":
    d1 = [1, 0]
    d2 = [0, 1]
    i = 0
    d0 = dn = d2
    y = [x1, x2]
    k = 0
    get_t(x1, x2, d2)
    #next_y = y + t0 * d0
