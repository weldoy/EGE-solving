def f(x, c):
    if x >= 58:
        return c % 2 == 0
    elif c == 0:
        return False

    return any([f(x + 1, c - 1), f(x + 4, c - 1), f(x * 2, c - 1)])


def f2(x, c):
    if x >= 58:
        return c % 2 == 0
    elif c == 0:
        return False

    elif c % 2 > 0:
        return any([f2(x + 1, c - 1), f2(x + 4, c - 1), f2(x * 2, c - 1)])
    return all([f2(x + 1, c - 1), f2(x + 4, c - 1), f2(x * 2, c - 1)])


print(19, [s for s in range(1, 58) if f2(s, 2)])
print(20, [s for s in range(1, 58) if f2(s, 3) and not f2(s, 1)])
print(21, [s for s in range(1, 58) if f2(s, 4) and not f2(s, 2)])
