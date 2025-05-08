f = open('9_3.csv')

count = 0
for i in f:
    x = sorted(list(map(int, i.split(';'))))
    print(x)
    bmax = x[2]**2
    another = x[0] * x[1] * 2
    if bmax > another:
        count += 1


print(count)
