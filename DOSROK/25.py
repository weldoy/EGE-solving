def f(n):
    divisors = set()
    for i in range(2, int(n**.5) + 1):
        if n % i == 0 and n != i:
            if (i % 10 == 7) and (i != 7):
                divisors.add(i)
            if ((n // i) % 10 == 7) and ((n // i) != 7):
                divisors.add(n // i)
    return min(divisors) if divisors else 0


count = 0
for o in range(1125000, 5000000):
    if f(o):
        count += 1
        print(o, f(o))
    if count == 5:
        break
