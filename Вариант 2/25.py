def prime(n):
    for x in range(2, int(n**.5) + 1):
        if n % x == 0:
            return False
    if n != 1:
        return True


def divisor(x):
    divisors = set()
    for o in range(2, int(x**.5) + 1):
        if x % o == 0:
            if prime(o):
                divisors.add(o)
            if prime(x // o):
                divisors.add((x // o))
    return sorted(divisors)


for i in range(456790, 457900):
    f = divisor(i)
    if f:
        if len(f) >= 4:
            M = f[0] + f[1] + f[-1] + f[-2]
            if M % 114 == 39:
                print(i, M)
        else:
            M = 0
