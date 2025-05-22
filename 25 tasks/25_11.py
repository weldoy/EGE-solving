def netr(x):
    b = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            if i % 2 != 0:
                b.add(i)
            if (x // i) % 2 != 0:
                b.add((x // i))
    return sorted(b)


count = 0
for n in range(200_000_000 + 1, 10**10):
    if len(netr(n)) >= 6:
        count += 1
        if count <= 5:
            print(n, netr(n)[-6])
