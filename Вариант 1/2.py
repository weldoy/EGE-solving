from itertools import *


def f(x, y, z, w):
    return (z <= y) or ((w <= x) <= y)


for x1, x2, x3, x4, x5, x6 in product([0, 1], repeat=6):
    t = (
        (x1, 0, 0, x2, 0),
        (x3, x4, 1, x5, 0),
        (x6, 1, 1, 1, 0)
    )
    if len(set(t)) == len(t):
        for p in permutations('xyzw', r=4):
            if all(f(**dict(zip(p, m))) == m[-1] for m in t):
                print(*p)
