from itertools import *


def f(x, y, z, w):
    return (not x and not y) or (x == z) or not w


for x1, x2, x3, x4 in product([0, 1], repeat=4):
    t = (
        (0, 1, x2, 1, 0),
        (1, x2, 0, 0, 0),
        (x3, 1, 0, x4, 0)
    )
    if len(t) == len(set(t)):
        for p in permutations('xyzw', r=4):
            if all(f(**dict(zip(p, m))) == m[-1] for m in t):
                print(*p)
