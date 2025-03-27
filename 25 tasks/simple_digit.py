def is_prime(a):
    if a % 2 == 0:
        return a == 2
    d = 3
    while d * d <= a and a % d != 0:
        d += 2
    return d * d > a


print(is_prime(int(input("Enter a number: "))))


def prime(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x**.5) + 1))


print(prime(3))
