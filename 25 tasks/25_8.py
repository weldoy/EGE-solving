def f(x: int):
    divisors = set()
    for i in range(2, int(x**.5) + 1):
        if x % i == 0 and x != i:
            if i % 10 == 9 and i != 9:
                divisors.add(i)
            if x // i != 9 and x // i % 10 == 9:
                divisors.add(x//i)
    if divisors:
        return min(divisors)  # Лучше сначала вернуть просто divisors


count = 0
for i in range(800_000, 800_000_000):
    if f(i):
        count += 1
        print(i, f(i))
    if count == 5:
        break
