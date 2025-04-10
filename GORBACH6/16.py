from sys import setrecursionlimit

setrecursionlimit(10000)

def f(n):
    return n if n < 52 else 3 * f(n-2) - n

print(f(15127) // f(15099))
