for i in range(4, 10000):
    n = '3' + '1' * i
    while '31' in n or '211' in n or '1111' in n:
        if '31' in n:
            n = n.replace('31', '1', 1)
        if '211' in n:
            n = n.replace('211', '13', 1)
        if '1111' in n:
            n = n.replace('1111', '2', 1)

    summa = 0
    for j in n:
        summa += int(j)
    if summa == 15:
        print(i, n, summa)
