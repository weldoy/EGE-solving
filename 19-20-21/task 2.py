def f19(x, y, c):
    if x + y >= 65:
        return c % 2 == 0
    elif c == 0:
        return False

    elif c % 2 > 0:
        return any([f19(x + 1, y, c - 1), f19(x * 3, y, c - 1), f19(x, y + 1, c - 1), f19(x, y * 3, c - 1)])
    return any([f19(x + 1, y, c - 1), f19(x * 3, y, c - 1), f19(x, y + 1, c - 1), f19(x, y * 3, c - 1)])


def f20_21(x, y, c):
    if x + y >= 65:
        return c % 2 == 0
    elif c == 0:
        return False

    elif c % 2 > 0:
        return any([f20_21(x + 1, y, c - 1), f20_21(x * 3, y, c - 1), f20_21(x, y + 1, c - 1), f20_21(x, y * 3, c - 1)])
    return all([f20_21(x + 1, y, c - 1), f20_21(x * 3, y, c - 1), f20_21(x, y + 1, c - 1), f20_21(x, y * 3, c - 1)])


print(19, [s for s in range(1, 59) if f19(6, s, 2)])
print(20, [s for s in range(1, 59) if f20_21(6, s, 3) and not f20_21(6, s, 1)])
print(21, [s for s in range(1, 59) if f20_21(6, s, 4) and not f20_21(6, s, 2)])
    