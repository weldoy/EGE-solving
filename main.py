def prime(n):
    for x in range(2, int(n**.5) + 1):
        if n % x == 0:
            return False
    if n != 1:
        return True


print(prime(2))
