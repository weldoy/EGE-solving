def f(x, y, cnt=0):
    if x == y:
        return 1
    elif x > y + 2:
        return 0
    else:
        return (f(x - 1, y, cnt + 1) if cnt < 2 else 0) + f(x + 5, y) + f(x * 2, y)


print(f(5, 34))
