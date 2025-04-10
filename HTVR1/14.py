arr = []

for x in range(1, 2031):
    n0 = 7**170 + 7**100 - x
    n = n0
    s = ''

    while n > 0:
        s += str(n % 7)
        n //= 7

    arr.append(s.count('0'))
    if s.count('0') == 73:
        print(x)

