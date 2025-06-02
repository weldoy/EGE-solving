f = open('9_22546.csv')

k = 0
for i in f:
    x = sorted(list(map(int, i.split(','))))
    if len(set(x)) == 7:
        if (x[0] * x[1]) <= (x[2] + x[3] + x[4] + x[5] + x[6]):
            k += 1

print(k)
