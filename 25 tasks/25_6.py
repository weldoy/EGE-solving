def m(number):
    divisors = set()
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            divisors.add(i)
            divisors.add(number // i)
    return max(divisors) + min(divisors)


count = 0
for i in range(800_000, 800_000_000):
    if m(i) % 10 == 4:
        print(i, m(i))
        count += 1
    if count == 5:
        break

