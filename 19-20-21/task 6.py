def f(x: int, y: int, cnt: int):
    if x + y >= 59:
        return cnt % 2 == 0
    if cnt == 0:
        return False
    return any([f(x + 1, y, cnt - 1), f(x * 2, y, cnt - 1), f(x, y + 1, cnt - 1), f(x, y * 2, cnt - 1)])


def f2(x: int, y: int, cnt: int):
    if x + y >= 59:
        return cnt % 2 == 0
    if cnt == 0:
        return False

    if cnt % 2 > 0:
        return any([f2(x + 1, y, cnt - 1), f2(x * 2, y, cnt - 1), f2(x, y + 1, cnt - 1), f2(x, y * 2, cnt - 1)])
    return all([f2(x + 1, y, cnt - 1), f2(x * 2, y, cnt - 1), f2(x, y + 1, cnt - 1), f2(x, y * 2, cnt - 1)])


print(19, [s for s in range(1, 54) if f(5, s, 2)])
print(20, [s for s in range(1, 54) if f2(5, s, 3) and not f2(5, s, 1)])
print(20, [s for s in range(1, 54) if f2(5, s, 4) and not f2(5, s, 2)])
