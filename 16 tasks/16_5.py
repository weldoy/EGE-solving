from sys import setrecursionlimit

setrecursionlimit(3000)


def f(n):
    return n if n >= 2025 else n + 3 + f(n+3)


print(f(23) - f(21))