def f(x, y):
    if (x < y) or x == 28:
        return 0
    elif x == y:
        return 1
    else:
        return f(x - 2, y) + (f(x / 2, y) if x % 2 == 0 else f(x - 3, y))


print(f(98, 1))
