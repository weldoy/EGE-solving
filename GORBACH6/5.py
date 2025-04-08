arr = []

for n0 in range(1, 1000):
    n = n0
    s = ''
    while n > 0:
        s += str(n%7)
        n //= 7
    s = s[::-1]

    if s.count('3') % 2 == 0:
        s = s + s[0]
        s = '3' + s
    else:
        s = s + s[-1]
        s = '6' + s

    if int(s, 7) < 16777:
        print(n0, int(s, 7))
        arr.append(int(s, 7))

print(max(arr))
