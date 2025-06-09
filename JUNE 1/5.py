for f in range(1, 1000):
    n = bin(f)[2:]
    if n.count('1') % 2 == 0:
        n = '11' + n[2:] + '1'
    else:
        if n.count('0') < n.count('1'):
            n = n + '0'
        else:
            n = n + '1'

    if int(n, 2) > 271:

        print(f, int(n, 2))
