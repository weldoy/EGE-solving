from math import *


def f(x, y, c):
    if x + y <= 42:
        return c % 2 == 0
    if c == 0:
        return False
    return any([f(ceil(x / 2), y, c - 1), f(ceil(x / 3), y, c - 1), f(x, ceil(y / 2), c - 1), f(x, ceil(y / 3), c - 1)])


def f2(x, y, c):
    if x + y <= 42:
        return c % 2 == 0
    if c == 0:
        return False
    if c % 2 > 0:
        return any([f2(ceil(x / 2), y, c - 1), f2(ceil(x / 3), y, c - 1), f2(x, ceil(y / 2), c - 1), f2(x, ceil(y / 3), c - 1)])
    return all([f2(ceil(x / 2), y, c - 1), f2(ceil(x / 3), y, c - 1), f2(x, ceil(y / 2), c - 1), f2(x, ceil(y / 3), c - 1)])


print(19, [s for s in range(50, 1000) if f(111, s, 3) and not f(111, s, 2)])
print(20, [s for s in range(50, 1000) if f2(111, s, 3) and not f2(111, s, 2)])
print(21, [s for s in range(50, 1000) if f2(111, s, 4) and not f2(111, s, 2)])
