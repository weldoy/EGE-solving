from itertools import permutations, product


def f(x, y, z, w):
    return not(x <= w) or (y <= z) or not(y)


for x1, x2, x3, x4, x5, x6, x7 in product([0, 1], repeat=7):
    t = (
        (x1, 1, x2, 0, 0),
        (x3, 0, 1, x4, 0),
        (x5, x6, 0, x7, 0)
    )
    if len(set(t)) == len(t):
        for p in permutations('xyzw', r=4):
            if all(f(**dict(zip(p, m))) == m[-1] for m in t):
                print(*p)
