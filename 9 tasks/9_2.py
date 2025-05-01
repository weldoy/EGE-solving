f = open('991.csv')
k = 0
for i in f:
    x = sorted(list(map(int, i.split(';'))))
    k += 1
    if len(set(x)) == 3:
        b1 = []
        b3 = []
        for j in x:
            if x.count(j) == 1:
                b1.append(j)
            if x.count(j) == 3:
                b3.append(j)
        if len(b1) == 1 and len(b3) == 6:
            if sum(b3) / 6 < b1[0]:
                print(k)