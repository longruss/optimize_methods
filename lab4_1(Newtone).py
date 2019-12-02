#Метод Ньютона
from math import sqrt
import numpy as np


eps = 0.001
old_x = [1, 2]
M = int(input("Введите предельное число итераций: "))


def func(x1, x2):
    return x1 ** 2 - x1 * x2 + x2 ** 2


def diff_x1(x1, x2):
    return (func(x1 + eps, x2) - func(x1, x2)) / eps


def diff_x2(x1, x2):
    return (func(x1, x2 + eps) - func(x1, x2)) / eps


def diff2_x1(x1, x2):
    return (func(x1 + eps, x2) - 2 * func(x1, x2) + func(x1 - eps, x2)) / (eps * eps)


def diff2_x2(x1, x2):
    return (func(x1, x2 + eps) - 2 * func(x1, x2) + func(x1, x2 - eps)) / (eps * eps)


def diff2_x1x2(x1, x2):
    return (func(x1 + eps, x2 + eps) - func(x1 + eps, x2 - eps) - func(x1 - eps, x2 + eps) + func(
        x1 - eps, x2 - eps)) / (4 * eps * eps)


def get_grad(base_x1, base_x2):
    x1 = base_x1
    x2 = base_x2
    return [diff_x1(x1, x2), diff_x2(x1, x2)]


def get_gesse(base_x1, base_x2):
    x1, x2 = base_x1, base_x2
    return [[diff2_x1(x1, x2), diff2_x1x2(x1, x2)], [diff2_x1x2(x1, x2), diff2_x2(x1, x2)]]


def get_length_of_grad(grad_arr):
    return sqrt(pow(grad_arr[0], 2) + pow(grad_arr[1], 2))


def invar_gesse(arr):
    return np.linalg.inv(arr)


def determ(arr):
    return np.linalg.det(arr)


if __name__ == "__main__":
    k = 0
    dk = []
    new_x = [0, 0]
    # print(get_gesse(old_x[0], old_x[1]))
    # print(invar_gesse(get_gesse(old_x[0], old_x[1])))
    # print(determ(get_gesse(old_x[0], old_x[1])))
    while k < M:
        print("Итерация № " + str(k))
        grad_arr = get_grad(old_x[0], old_x[1])
        if get_length_of_grad(grad_arr) < eps:
            break
        g = get_gesse(old_x[0], old_x[1])
        g_inv = invar_gesse(g)
        dk = np.dot(g_inv * (-1), grad_arr)
        new_x[0], new_x[1] = old_x[0] + dk[0], old_x[1] + dk[1]
        if sqrt(pow(new_x[0], 2) + pow(new_x[1], 2)) - sqrt(pow(old_x[0], 2) + pow(new_x[1], 2)) > eps or \
                abs(func(new_x[0], new_x[1]) - func(old_x[0], old_x[1])) > eps:
            k += 1
            old_x = new_x
            continue
        elif sqrt(pow(new_x[0], 2) + pow(new_x[1], 2)) - sqrt(pow(old_x[0], 2) + pow(new_x[1], 2)) < eps and \
                abs(func(new_x[0], new_x[1]) - func(old_x[0], old_x[1])) < eps:
            old_x[0], old_x[1] = new_x[0], new_x[1]
            break
    print("x1 = " + str(old_x[0]) + " x2 = " + str(old_x[1]) + " func(x1, x2) = " + str(func(old_x[0], old_x[1])))
