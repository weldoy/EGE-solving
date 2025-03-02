for n in range(1, 100):
    n1 = str(bin(n)[2:])
    n1 += str(n1.count('1') % 2)
    n1 += str(n1.count('1') % 2)
    print(n, int(n1, 2))
