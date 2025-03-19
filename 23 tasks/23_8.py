def f(x, y):
    if x > y:
        return 0
    elif x == y:
        return 1
    else:
        return f(x+2, y) + f(x+5, y) + (f(x**2, y) if x < (35**0.5) else 0)


print(f(4, 36))
