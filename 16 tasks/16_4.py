from sys import setrecursionlimit

setrecursionlimit(3000)


def f(n):
    return 1 if n == 1 else f(n-1) * (n+1) 


print(f(5))