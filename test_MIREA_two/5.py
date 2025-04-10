for n0 in range(1, 100):
    n = n0
    s = ''

    while n > 0:
        s += str(n % 2)
        n //= 2
    s = s[::-1]

    if int(s) % 4 == 0:
        s += '00'
    if int(s) % 4 == 1:
        s += '01'
    if int(s) % 4 == 2:
        s += '10'
    if int(s) % 4 == 3:
        s += '11'

    print(n0, s, int(s, 2))
