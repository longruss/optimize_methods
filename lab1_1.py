def func(x):
    if x == 0:
        return 0
    else:
        return 5 + x ** 2 + 1 / x


if __name__ == "__main__":
    a = float(input("Введите начало отрезка "))
    b = float(input("Введите конец отрезка "))
    c = 0
    eps = float(input("Введите точность "))
    print(func(a))
    print(func(b))
    while abs(b - a) > eps:
        c = (a + b) / 2
        f1 = func(c - eps)
        f2 = func(c + eps)
        if f1 < f2:
            b = c
            #print(func(c))
        elif f1 > f2:
            a = c
            #print(func(c))

    print(c)
    #print(func(c))
