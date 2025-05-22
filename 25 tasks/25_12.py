def prime(n):
    for d in range(2, int(n**.5) + 1):
        if n % d == 0:
            return False
    if n != 1:
        return True


def divisors(x):
    b = set()
    for i in range(2, int(x**.5) + 1):
        if x % i == 0:
            if prime(i):
                b.add(i)
            if prime(x//i):
                b.add((x//i))
    return sorted(b)


count = 0
for i in range(1_200_001, 10**10):
    if len(divisors(i)) > 0:
        M = divisors(i)[0] + divisors(i)[-1]
        if M > 2000 and M % 10 == 8:
            count += 1
            if count <= 5:
                print(i, M)
            else:
                break
