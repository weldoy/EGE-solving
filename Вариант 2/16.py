from sys import setrecursionlimit
setrecursionlimit(100000)


def f(x):
    return 66 if x < 1000 else f(x - 5) + 100


print(f(180000)-f(100000))
