from itertools import product, permutations


def f(x, y, z, w):
    return (x and y) or (y == z) or w


for x1, x2, x3, x4 in product([0, 1], repeat=4):
    t = (
        (x1, 1, 0, 0, 0),
        (0, x2, 1, x3, 0),
        (0, 1, x4, 1, 0)
    )
    if len(t) == len(set(t)):
        for p in permutations('xyzw', r=4):
            if all(f(**dict(zip(p, m))) == m[-1] for m in t):
                print(*p)
