#  Делители


def is_prime(number):  # Проверка на простое число
    if number % 2 == 0 and number != 2:
        return False
    for o in range(3, int(number**.5) + 1, 2):
        if number % o == 0:
            return False
    return True


def r(n):
    divisors = set()
    for a in range(2, int(n**.5) + 1):
        if n % a == 0:
            divisors.add(a)
            divisors.add(n // a)
    return sum(divisors)


count = 0
for i in range(500_000, 500_000_000):
    if r(i) % 10 == 9:
        count += 1
        print(f'{i=} {r(i)=}')
    if count == 5:
        break
