def f(x, y):
    if (x > y) or x == 27:
        return 0
    if x == y:
        return 1
    return f(x + 3, y) + f(x + 5, y) + f(x**2, y)


print(f(3, 16) * f(16, 51))
