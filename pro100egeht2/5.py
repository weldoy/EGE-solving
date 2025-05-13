for a in range(1, 100):
    n = a

    n2 = bin(n)[2:]
    if (n2.count('0') + n2.count('1')) % 2 == 0:
        n2 = n2[:(len(n2) // 2)] + '1' + n2[(len(n2) // 2):]
    else:
        n2 = n2

    print(a, n2, int(n2, 2))
