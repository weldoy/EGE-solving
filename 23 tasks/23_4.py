def f(x, y):
    if (x < y) or x == 24:
        return 0
    elif x == y:
        return 1
    else:
        return f(x - 1, y) + f(int(x**0.5), y) + (f(int(str(x)[0:-1]), y) if x > 9 else 0)


print(f(602, 7))
