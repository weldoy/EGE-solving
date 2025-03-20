def f2(x, c):
    if x >= 39:
        return c % 2 == 0
    if c == 0:
        return False
    if c % 2 > 0:
        return any([f2(x + 1, c - 1), f2(x + 3, c - 1), f2(x * 2, c - 1)])
    return all([f2(x + 1, c - 1), f2(x + 3, c - 1), f2(x * 2, c - 1)])


print(19, [s for s in range(1, 39) if f2(s, 2)])
print(20, [s for s in range(1, 39) if f2(s, 3) and not f2(s, 1)])
print(21, [s for s in range(1, 39) if f2(s, 4) and not f2(s, 2)])
