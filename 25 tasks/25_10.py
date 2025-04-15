def f(x):
    divisors = set()
    for i in range(2, int(x**.5) + 1):
        if x % i == 0:
            if i % 10 == 9 and i != 9:
                divisors.add(i)
            if (x // i) % 10 == 9 and (x // i) != 9:
                divisors.add(x // i)
    return min(divisors) if divisors else 0


for o in range(600_000, 1_000_000):
    if f(o):
        print(o, f(o))
