from itertools import product, permutations


def f(x, y, z, w):
    return y and (x <= w) and ((not x) <= ((not w) == z))


for x1, x2, x3, x4, x5 in product([0, 1], repeat=5):
    t = (
        (0, 0, x1, x2, 1),
        (0, x3, x4, 0, 1),
        (1, 1, 1, x5, 0)
    )
    if len(t) == len(set(t)):
        for p in permutations('xyzw', r=4):
            if all(f(**dict(zip(p, m))) == m[-1] for m in t):
                print(*p)
