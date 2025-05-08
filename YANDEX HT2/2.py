from itertools import *


def f(x, y, z, w):
    return ((not x) <= z) and (w or (not y)) and (not z)


for x1, x2, x3, x4, x5, x6 in product([0, 1], repeat=6):
    t = (
        (0, 1, 1, x1, 1),
        (1, x2, x3, 0, 1),
        (x4, 0, x5, x6, 1)
    )
    if len(t) == len(set(t)):
        for p in permutations('xyzw', r=4):
            if all(f(**dict(zip(p, m))) == m[-1] for m in t):
                print(*p)
