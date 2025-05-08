f = open('313_9.csv')

count = 0
for i in f:
    x = sorted(list(map(int, i.split(';'))))
    if len(set(x)) == 5:
        b1 = []
        b3 = []
        for j in x:
            if x.count(j) == 1:
                b1.append(j)
            if x.count(j) == 3:
                b3.append(j)
        if len(b3) == 3 and len(b1) == 4:
            if (sum(b1) / 4) >= (sum(b3) / 3):
                count += 1

print(count)
