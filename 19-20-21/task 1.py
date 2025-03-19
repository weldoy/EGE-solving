def f(x: int, cnt: int) -> int:
    if x >= 132:
        return cnt % 2 == 0
    if cnt == 0:
        return False

    if cnt % 2 > 0:
        return any([f(x + 3, cnt - 1), f(x + 6, cnt - 1), f(x * 3, cnt - 1)])
    return all([f(x + 3, cnt - 1), f(x + 6, cnt - 1), f(x * 3, cnt - 1)])


def f2(x: int, cnt: int) -> int:
    if x >= 132:
        return cnt % 2 == 0
    if cnt == 0:
        return False

    if cnt % 2 > 0:
        return any([f(x + 3, cnt - 1), f(x + 6, cnt - 1), f(x * 3, cnt - 1)])
    return any([f(x + 3, cnt - 1), f(x + 6, cnt - 1), f(x * 3, cnt - 1)])


print(19, [s for s in range(1, 132) if f(s, 2)])
print(20, [s for s in range(1, 132) if f2(s, 3) and not f2(s, 1)])
print(21, [s for s in range(1, 132) if f2(s, 4) and f2(s, 2)])
