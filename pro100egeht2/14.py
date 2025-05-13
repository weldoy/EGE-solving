def from64(n):
    summa = 0
    n = str(n)[::-1]
    for i in range(len(n)):
        for j in n:
            summa += int(j) * 64**i
    return summa


for x in range(64):
    n = from64(f'98{x}16') + from64(f'17{x}12')
    if n % 63 == 0:
        print(n // 63, x)
