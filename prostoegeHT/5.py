for n0 in range(1, 1000):

    n = bin(n0)[2:]

    if n.count('1') % 2 == 0:
        n = '10' + n[2:] + '0'
    else:
        n = '11' + n[2:] + '1'

    print(n0, int(n, 2))
