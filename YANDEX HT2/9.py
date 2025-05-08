f = open('9.csv')
count = 0

for i in f:
    x = sorted(list(map(int, i.split(';'))))
    b2 = []
    b1 = []
    for b in x:
        if x.count(b) == 2:
            b2.append(b)
        if x.count(b) == 1:
            b1.append(b)
    if ((len(b1) == 1) and (b1[0] != x[0]) and (b1[0] != x[6])) and len(b2) == 6:
        count += 1

print(count)
