for n0 in range(1, 1000):
    n = bin(n0)[2:]

    if n0 % 2 == 0:
        n = n.replace('0', '1')
    else:
        n = n[0] + n[1:].replace('1', '00')

    if int(n, 2) <= 600:
        print(n0, int(n, 2))
