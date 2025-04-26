def f(x, y):
    if x > y or ('6' in str(x)):
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x + 3, y)


print(f(1, 45))
