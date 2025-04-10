from itertools import product, permutations


def f(x, y, z, w):
    return (z == (not y)) and (not x or y) and w


for x1, x2, x3, x4, x5, x6 in product([0, 1], repeat=6):
    t = (
        (1, x1, x2, 0, 1),
        (0, 0, x3, 1, 1),
        (x4, x5, x6, 1, 1)
    )
    if len(t) == len(set(t)):
        for p in permutations('xyzw', r=4):
            if all(f(**dict(zip(p, m))) == m[-1] for m in t):
                print(*p)
