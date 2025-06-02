def f(x, c):
    if x >= 471:
        return c % 2 == 0
    if c == 0:
        return False
    if c % 2 > 0:
        return any([f(x + 4, c - 1), f(x + 7, c - 1), f(x * 4, c - 1)])
    return all([f(x + 4, c - 1), f(x + 7, c - 1), f(x * 4, c - 1)])


print(19, [s for s in range(1, 471) if f(s, 2)])
print(20, [s for s in range(1, 471) if f(s, 3) and not f(s, 1)])
print(21, [s for s in range(1, 471) if f(s, 4) and not f(s, 2)])

