for n in range(1, 100):

    n1 = str(bin(n)[2:])
    if n1.count('1') % 2 == 0:
        n1 += '0'
        n1 = '10' + n1[2:]
    else:
        n1 += '1'
        n1 = '11' + n1[2:]
    n1 = int(n1, 2)

    if n1 >= 50:
        print(f'r={n1}, {n=}')
        break
