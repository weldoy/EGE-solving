for n0 in range(1, 13):
    n = n0
    s = ''

    while n > 0:
        s += str(n % 2)
        n //= 2
    s = s[::-1]

    if int(s) % 2 == 0:
        s = '10' + s
    else:
        s = '1' + s + '01'

    print(n0, s, int(s, 2))
