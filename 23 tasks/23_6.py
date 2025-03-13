def f(x, y, c=0, a=0):
    if x < y:
        return 0
    elif x == y:
        return 1
    else:
        return (f(x - 2, y, c=c+1, a=0) if c < 2 else 0) + \
            (f(x // 2, y, c=0, a=a+1) if x % 2 == 0 else (f(x - 7, y, c=0, a=a+1) if a < 2 else 0))


print(f(40, 1))
