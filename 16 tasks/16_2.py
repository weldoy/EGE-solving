from sys import setrecursionlimit

setrecursionlimit(3000)


def f(n):
    return 10 if n < 11 else n + f(n - 1)


print(f(2024) - f(2022))
