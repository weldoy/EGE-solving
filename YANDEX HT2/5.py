def summa(x):
    a = 0
    for i in x:
        a += int(i)
    return a


arr = []

for n0 in range(483, 1000):
    n = n0

    n8 = oct(n)[2:]
    s8 = summa(n8)

    if s8 % 2 == 0:
        n8 += oct(s8)[2:]
    else:
        n8 = oct(s8)[2:] + n8

    arr.append(int(n8, 8))
    print(n0, int(n8, 8))

print(min(arr))

