# НЕВЕРНО РЕШЕН!


def is_prime(number):
    return number > 1 and all(number % i != 0 for i in range(2, int(number**.5) + 1))


def divisors_x(x):
    divisors = set()
    for i in range(2, int(x**.5) + 1):
        if is_prime(i):
            if x % i == 0:
                divisors.add(i)

        if is_prime(x // i):
            if (x // i) % i == 0:
                divisors.add(x // i)

    return sum(divisors) if divisors else 0


count = 0
for x in range(550_000, 1_000_000):
    if divisors_x(x) % 10 == 1:
        count += 1
        print(x, divisors_x(x))
    if count == 5:
        break
