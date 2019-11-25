import math


prop = (1 + math.sqrt(5)) / 2


def func(x):
    return 5 - x ** 2 + 1 / x


if __name__ == "__main__":
    a = float(input("Введите начало отрезка "))
    b = float(input("Введите конец отрезка "))
    eps = float(input("Введите точность "))
    x = 0
    while abs(b - a) > eps:
        x1 = b - ((b - a) / prop)
        x2 = a + ((b - a) / prop)
        y1 = func(x1)
        y2 = func(x2)
        if y1 >= y2:
            a = x1
            print(x1)
        else:
            b = x2
            print(x2)
    x = (a + b) / 2
    fx = func(x)
    print(x)
    print(fx)
