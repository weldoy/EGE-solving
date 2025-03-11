for x in range(8300, 10000):
    n = 5**100 - x
    s = ''
    while n > 0:
        s += str(n % 5)
        n //= 5
    if s.count('0') == 4:
        print(x)
