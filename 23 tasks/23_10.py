b = set()

from functools import lru_cache


@lru_cache(None)
def f(x, k=0):
    if k < 68:
        f(x + 3, k + 1)
        f(x - 2, k + 1)
    if k == 68:
        b.add(x)


f(1)
print(len(b))
