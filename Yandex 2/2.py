import itertools

count = 0


def f(a, b, c, d):
    return (a <= b) and (b <= c) and (c <= d)


for x1, x2 in itertools.product([0, 1], repeat=2):
    t = (
        (0, x1, 1, 0, 1),
        (0, x2, 1, 0, 1),
        (0, 1, 1, 1, 1)
    )
    if len(set(t)) == len(t):
        for p in itertools.permutations('abcd', r=4):
            count += 1
            if all(f(**dict(zip(p, m))) == m[-1] for m in t):
                print(*p)
