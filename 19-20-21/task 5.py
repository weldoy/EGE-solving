def f(x, y, c):
    if x + y >= 227:
        return c % 2 == 0
    if c == 0:
        return False
    if c % 2 > 0:
        return any([f(x + 1, y, c - 1), f(x * 2, y, c - 1), f(x, y + 1, c - 1), f(x, y * 2, c - 1)])
    return any([f(x + 1, y, c - 1), f(x * 2, y, c - 1), f(x, y + 1, c - 1), f(x, y * 2, c - 1)])


def f2(x, y, c):
    if x + y >= 227:
        return c % 2 == 0
    if c == 0:
        return False
    if c % 2 > 0:
        return any([f2(x + 1, y, c - 1), f2(x * 2, y, c - 1), f2(x, y + 1, c - 1), f2(x, y * 2, c - 1)])
    return all([f2(x + 1, y, c - 1), f2(x * 2, y, c - 1), f2(x, y + 1, c - 1), f2(x, y * 2, c - 1)])

