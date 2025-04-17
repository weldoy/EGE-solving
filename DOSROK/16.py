from sys import setrecursionlimit
setrecursionlimit(3000)


def f(n):
    return 1 if n <= 5 else n + f(n - 2)


print(f(2126) - f(2122))
