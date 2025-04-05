def f(x, y):
    if (x > y) or x == 0:
        return 0
    if x == y:
        return 1
    return f(x + 3, y) + f(x + 4, y) + f(abs(x), y)


print(f(-21, -8) * f(-8, 35))
