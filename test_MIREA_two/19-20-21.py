def f(a, c):
    if a >= 40:
        return c % 2 == 0
    if c == 0:
        return False
    if c % 2 > 0:
        return any([f(a + 2, c - 1), f(a * 2, c - 1)])
    return all([f(a + 2, c - 1), f(a * 2, c - 1)])


def f19(a, c):
    if a >= 40:
        return c % 2 == 0
    if c == 0:
        return False
    return any([f19(a + 2, c - 1), f19(a * 2, c - 1)])


print(19, [s for s in range(1, 38) if f19(s, 2)])
print(20, [s for s in range(1, 38) if f(s, 3) and not f(s, 1)])
print(21, [s for s in range(1, 38) if f(s, 4) and not f(s, 2)])

