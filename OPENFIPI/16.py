from sys import setrecursionlimit

setrecursionlimit(10000)


def f(x):
    return x if x >= 2025 else x * 2 + f(x + 2)


print(f(82)-f(81))
