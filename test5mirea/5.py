for n0 in range(1, 100):
    n = n0

    n = n - (n % 4)
    n = bin(n)[2:]
    n = n + str(n.count('1') % 2)
    n = n + str(n.count('1') % 2)

    if int(n, 2) > 100:
        print(n0, n, int(n, 2))
