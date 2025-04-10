def r(n):
    divisors = set()
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
        return sum(divisors)


count = 0
for n in range(500_000, 5_000_000):
    if r(n) % 10 == 9:
        count += 1
        print(n, r(n))
    if count == 5:
        break
