for n1 in range(1, 500):
    n = n1
    n = '7'*n + '8'*n + '9'*n

    while '78' in n or '98' in n or '999' in n:
        if '78' in n:
            n = n.replace('78', '8', 1)
        if '98' in n:
            n = n.replace('98', '7', 1)
        if '999' in n:
            n = n.replace('999', '9', 1)

    summa = 0
    for i in n:
        summa += int(i)
    print(summa, n1)
