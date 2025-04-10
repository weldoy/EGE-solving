
for x in range(1, 2030):
    n0 = 3**100 - x
    n = n0
    s = ''
    while n > 0:
        s += str(n % 3)
        n //= 3
    if s.count('0') == 5:
        print(x, int(s, 3))
