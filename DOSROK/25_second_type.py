counter = 0

for number in range(1125000, 5_000_000):
    divisors = set()
    for divisor in range(2, int(number**.5) + 1):  # отсекает возможность того, что делитель равен числу
        if number % divisor == 0:
            if divisor % 10 == 7 and divisor != 7:
                divisors.add(divisor)
            pare = number // divisor
            if pare % 10 == 7 and pare != 7:
                divisors.add(pare)
    if divisors:
        print(number, min(divisors))
        counter += 1
        if counter == 5:
            break
