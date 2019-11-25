# Метод случайного поиска с возвратом при неудачном шаге

import numpy as np
import math


def func(x1, x2):
    return x1 ** 2 - x1 * x2 + x2 ** 2


def xi_update():
    # Находим вектор кси
    xi = np.random.uniform(-1, 1, 2)
    new_xi = []
    xi_length = 0
    # Вычисляем норму вектора кси
    for i in xi:
        xi_length += i ** 2
    xi_length = math.sqrt(xi_length)
    for xi_i in xi:
        new_xi.append(xi_i / xi_length)
    return new_xi


if __name__ == "__main__":
    # y1, y2 = 0, 0
    # Задаем начальные условия
    x1, x2 = 1, 2
    N = 50
    M = 50
    k = 0
    j = 1
    R = 0.001
    t = 2
    beta = 0.2
    # Тело метода
    while True:
        # Задаем вектор кси
        new_xi = xi_update()
        # Находим координаты новой точки
        y1 = x1 + t * new_xi[0]
        y2 = x2 + t * new_xi[1]
        # Проверка условий
        if func(y1, y2) < func(x1, x2):
            x1, x2 = y1, y2
            k += 1
            if k < N:
                j = 1
            elif k == N:
                break
        else:
            if j < M:
                j += 1
            elif j == M:
                if t <= R:
                    break
                else:
                    t *= beta
                    j = 1

    print(x1)
    print(x2)
    print(func(x1, x2))
#    test = 0
#    for m in new_xi:
#       test += m ** 2
