def f(a, b, c):
    if a + b >= 132:
        return c % 2 == 0
    if c == 0:
        return False
    return any([f(a + 2, b, c - 1), f(a * 2, b, c - 1), f(a * 3, b, c - 1),
                f(a, b + 2, c - 1), f(a, b * 2, c - 1), f(a, b * 3, c - 1)])


def f2(a, b, c):
    if a + b >= 132:
        return c % 2 == 0
    if c == 0:
        return False
    if c % 2 > 0:
        return any([f2(a + 2, b, c - 1), f2(a * 2, b, c - 1), f2(a * 3, b, c - 1),
                    f2(a, b + 2, c - 1), f2(a, b * 2, c - 1), f2(a, b * 3, c - 1)])
    return all([f2(a + 2, b, c - 1), f2(a * 2, b, c - 1), f2(a * 3, b, c - 1),
                f2(a, b + 2, c - 1), f2(a, b * 2, c - 1), f2(a, b * 3, c - 1)])


print(19, [s for s in range(1, 100) if f2(31, s, 2)])
print(20, [s for s in range(1, 100) if f2(31, s, 3) and not f2(31, s, 1)])
print(21, [s for s in range(1, 100) if f2(31, s, 4) and not f2(31, s, 2)])

