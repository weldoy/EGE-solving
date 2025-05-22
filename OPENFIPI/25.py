def f(x):
    divisors = set()
    for i in range(2, int(x**.5) + 1):
        if x % i == 0:
            divisors.add(i)
        pare = x // i
        if pare % i == 0:
            divisors.add(pare)
    if divisors:
        return sum(divisors)


count = 0
for a in range(500_000, 5_000_000):
    if f(a) and f(a) % 10 == 6:
        count += 1
        print(a, f(a))
    if count == 5:
        break


