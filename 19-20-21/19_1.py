def f(a: int, s: int, count: int):
    if count == 0 and a + s >= 81:
        return count % 2 == 0
    elif (count == 0 and (a + s < 81)) or ((a + s >= 81) and count > 0):
        return False

    elif count % 2 > 0:
        return any([f(a + 2, s, count - 1), f(a * 2, s, count - 1), f(a, s * 2, count - 1), f(a, s + 2, count - 1)])
    return all([f(a + 2, s, count - 1), f(a * 2, s, count - 1), f(a, s * 2, count - 1), f(a, s + 2, count - 1)])


print([s for s in range(1, 73) if f(7, s, 2)])
