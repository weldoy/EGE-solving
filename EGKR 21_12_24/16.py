# ЕГКР 21.12.24

from sys import setrecursionlimit

setrecursionlimit(5000)

def f(n):
    return n if n < 5 else 2 * n * f(n - 4)


print((f(13766) - 9 * f(13762)) / f(13758))
