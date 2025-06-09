def f(x, y):
    if x < y or x == 12:
        return 0
    if x == y:
        return 1
    return f(x - 3, y) + f(x // 2, y)


print(f(80, 23) * f(23, 3))
