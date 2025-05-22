def prime(x):
    for i in range(2, int(x**.5) + 1):
        if x % i == 0:
            return False
    if x != 1:
        return True


def divisors(x):
    b = set()
    for i in range(2, int(x**.5) + 1):
        if x % i == 0:
            if prime(i):
                b.add(i)
            if prime(x//i):
                b.add(x//i)
    return sorted(b)


count = 0
for i in range(500_000 - 1, 1, -1):
    if len(divisors(i)) > 0:
        S = sum(divisors(i))
        if S != 0 and S % 10 == 0:
            count += 1
            if count <= 5:
                print(i, S)
            else:
                break
