for n in range(1, 1000):
    n1 = str(bin(n)[2:])
    if n % 2 == 0:
        n1 += '0'*(n1.count('1') + n1.count('0'))
    elif n % 2 == 1:
        n1 += '1'*(n1.count('1') + n1.count('0'))

    print(n, int(n1, 2))
