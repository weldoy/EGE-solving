for n0 in range(1, 300):
    n = bin(n0)[2:]

    if n.count('1') % 2 == 0:
        n = '11' + n[2:] + '1'
    else:
        if n.count('1') > n.count('0'):
            n = n + '0'
        else:
            n = n + '1'
    if int(n, 2) >= 271:
        print(n0, int(n, 2))

