from sys import setrecursionlimit

setrecursionlimit(3000)


def f(n):
    if n == 1: return 1
    if n > 1 and n % 2 != 0: return n + f(n - 2)
    else: return n * f(n - 1)


print(f(40))
