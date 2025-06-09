from sys import *
from functools import lru_cache

setrecursionlimit(10000)


@lru_cache(None)
def f(n):
    return n**n**2 if n <= 1000 else n + 2*f(n - 2) + 6*f(n - 6)


for x in range(20100):
    f(x)

print(f(20024) - 2*f(20022) - 3*f(20020) + 18*f(20014))
