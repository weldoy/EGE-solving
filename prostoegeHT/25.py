def prime(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x**.5) + 1))


def f(x):
    divisors = set()
    for i in range(2, int(x**.5) + 1):
        if x % i == 0:
            if prime(i) and i % 10 == 1:
                divisors.add(i)
        if (x // i) % i == 0:
            if prime((x // i)) and (x // i) % 10 == 1:
                divisors.add(x // i)
    if divisors:
        return divisors


for i in range(26868, 32021 + 1):
    if f(i):
        if len(f(i)) >= 3:
            print(f(i))
            print(i, max(f(i)))



