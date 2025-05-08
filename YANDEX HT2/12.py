for x in range(5, 9999):
    n = (x * '1') + '7'

    while ('117' in n) or ('17' in n):
        if '117' in n:
            n = n.replace('117', '73', 1)
        else:
            n = n.replace('17', '1117', 1)

    print(x, n)
