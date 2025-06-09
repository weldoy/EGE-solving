from itertools import *


def f(x, y, z, w):
    return (y == (not w)) <= (not(w and (x == (x or (w <= z)))))


for x1, x2, x3, x4, x5, x6, x7, x8, x9, x10 in product([0, 1], repeat=10):
    t = (
        (x1, x2, 1, 1, 0),
        (x3, x4, 1, x5, 0),
        (x6, 1, x7, 1, 0),
        (1, x8, x9, x10, 1)
    )
    if len(t) == len(set(t)):
        for p in permutations('xyzw', r=4):
            if all(f(**dict(zip(p, m))) == m[-1] for m in t):
                print(*p)
