from sys import *
setrecursionlimit(10000)


def f(x):
    return x if x < 20 else (x - 6) * f(x - 7)


print((f(47872) - 290 * f(47865)) / f(47858))
