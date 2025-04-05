def f(x, y, c):
    if x + y >= 77:
        return c % 2 == 0
    if c == 0:
        return False

    return any([f(x + 3, y, c - 1), f(x * 3, y, c - 1), f(x, y + 3, c - 1), f(x, y * 3, c - 1)])


def f2(x, y, c):
    if x + y >= 77:
        return c % 2 == 0
    if c == 0:
        return False

    if c % 2 > 0:
        return any([f2(x + 3, y, c - 1), f2(x * 3, y, c - 1), f2(x, y + 3, c - 1), f2(x, y * 3, c - 1)])
    return all([f2(x + 3, y, c - 1), f2(x * 3, y, c - 1), f2(x, y + 3, c - 1), f2(x, y * 3, c - 1)])


print(19, [s for s in range(1, 64) if f(12, s, 2) and not f(12, s, 1)])
print(20, [s for s in range(1, 64) if f2(12, s, 3) and not f2(12, s, 1)])
print(21, [s for s in range(1, 64) if f2(12, s, 4) and not f2(12, s, 2)])
