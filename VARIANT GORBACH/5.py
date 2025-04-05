for n in range(1, 1000):
    nw = n
    n7 = ''
    while nw > 0:
        n7 += f'{nw % 7}'
        nw //= 7
    n7 = n7[::-1]
    if n7.count('3') > 0:
        if n7.count('3') % 2 == 0:
            n7 += n7[0]
            n7 = '3' + n7
        else:
            n7 = '6' + n7
            n7 += n7[-1]
    r = int(n7, 7)

    if r >= 16000:
        print(f'{n=} {n7=} {r=}')
