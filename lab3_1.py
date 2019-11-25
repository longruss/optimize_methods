# Метод градиентного спуска
from sympy import diff, symbols
from math import sqrt

eps = 0.001
old_x = [1, 2]
#alpha = 0.5
M = 10


def func(x1, x2):
    return x1 ** 2 - x1 * x2 + x2 ** 2


def derivative_1(base_x1, base_x2):
    x1, x2 = symbols('x1 x2')
    der_1 = diff(x1 ** 2 - x1 * x2 + x2 ** 2, x1)
    return int((der_1.subs([(x1, base_x1), (x2, base_x2)])))


def derivative_2(base_x1, base_x2):
    x1, x2 = symbols('x1 x2')
    der_2 = diff(x1 ** 2 - x1 * x2 + x2 ** 2, x2)
    return int(der_2.subs([(x1, base_x1), (x2, base_x2)]))


def get_grad(base_x1, base_x2):
    x1 = base_x1
    x2 = base_x2
    grad = [derivative_1(x1, x2), derivative_2(x1, x2)]
    return grad


def grad_condition_check(grad_arr):
    if sqrt(pow(grad_arr[0], 2) + pow(grad_arr[1], 2)) > eps:
        return True


def get_length_of_grad(grad_arr):
    return sqrt(pow(grad_arr[0], 2) + pow(grad_arr[1], 2))


def new_x_get(old_x, step, grad_arr):
    new_x = []
    old_x1, old_x2 = old_x[0], old_x[1]
    t = step
    grad_1, grad_2 = grad_arr[0], grad_arr[1]
    new_x.append(old_x1 - t * grad_1)
    new_x.append(old_x2 - t * grad_2)
    return new_x


if __name__ == "__main__":
    new_x = []
    k = 0
    t = float(input("Введите величину шага: "))
    while grad_condition_check(get_grad(old_x[0], old_x[1])) and k <= M:
        new_x = new_x_get(old_x, t, get_grad(old_x[0], old_x[1]))
        if func(new_x[0], new_x[1]) - func(old_x[0], old_x[1]) > 0 or \
                func(new_x[0], new_x[1]) - func(old_x[0], old_x[1]) > -eps * get_length_of_grad(old_x):
            t /= 2
            continue
        if sqrt(pow(new_x[0]-old_x[0], 2) + pow(new_x[1]-old_x[1]))
        print(new_x)
#        print(get_grad(x[0], x[1]))
#        print(grad_condition_check(get_grad(x[0], x[1])))
