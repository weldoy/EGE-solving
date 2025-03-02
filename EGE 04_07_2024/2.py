from itertools import product, permutations


def f(x, y, z, w):
    return (z <= (not(y <= x))) or w


for x1, x2, x3, x4, x5, x6, x7 in product([0, 1], repeat=7):
    t = (
        (x1, 1, x2, x3, 0),
        (x4, x5, 0, 0, 0),
        (x6, 0, 1, x7, 0)
    )
    if len(set(t)) == len(t):
        for p in permutations('xyzw', r=4):
            if all(f(**dict(zip(p, m))) == m[-1] for m in t):
                print(*p)
