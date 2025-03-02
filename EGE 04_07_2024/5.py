for n in range(28, 100):
    n2 = str(bin(n)[2:])
    if n2.count('1') % 2 == 0:
        n2 += '0'
        n2 = '10' + n2[2:]
    else:
        n2 += '1'
        n2 = '11' + n2[2:]
    n2 = int(n2, 2)
    print(f'{n=} {n2=}')
