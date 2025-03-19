def f19(a: int, s: int, count: int):
    if a + s >= 81:
        return count % 2 == 0
    if count == 0:
        return False

    if count % 2 > 0:
        return any([f19(a + 1, s, count - 1), f19(a * 2, s, count - 1), f19(a, s * 2, count - 1), f19(a, s + 1, count - 1)])
    return any([f19(a + 1, s, count - 1), f19(a * 2, s, count - 1), f19(a, s * 2, count - 1), f19(a, s + 1, count - 1)])


def f(a: int, s: int, count: int):
    if a + s >= 81:
        return count % 2 == 0
    if count == 0:
        return False

    if count % 2 > 0:
        return any([f(a + 1, s, count - 1), f(a * 2, s, count - 1), f(a, s * 2, count - 1), f(a, s + 1, count - 1)])
    return all([f(a + 1, s, count - 1), f(a * 2, s, count - 1), f(a, s * 2, count - 1), f(a, s + 1, count - 1)])


print(19, [s for s in range(1, 73) if f19(7, s, 2)])
print(20, [s for s in range(1, 73) if f(7, s, 3) and not f(7, s, 1)])
print(21, [s for s in range(1, 73) if f(7, s, 4) and not f(7, s, 2)])
