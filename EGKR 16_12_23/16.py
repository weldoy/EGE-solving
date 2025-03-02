# ЕГКР 16.12.23

from sys import setrecursionlimit

setrecursionlimit(5000)

def f(n):
    return 1 if n <= 3 else (n + 3) * f(n - 2)


print(f(2028) / f(2024))
