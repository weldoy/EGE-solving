def f(x, c):
    if x >= 100:
        return c % 2 == 0
    if c == 0:
        return False
    return all(f(int(str(str(x)[:-2] + str(x-1 + x))), c-1))


print(19, [s for s in range(14, 99) if f(s, 2)])
print(20, [s for s in range(14, 99) if f(s, 3) and not f(s, 1)])
print(21, [s for s in range(14, 99) if f(s, 4) and not f(s, 2)])
