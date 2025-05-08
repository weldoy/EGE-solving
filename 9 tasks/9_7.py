f = open('9_7.csv')

count = 0

for i in f:
    x = sorted(list(map(int, i.split(';'))))
    count += 1
    # print(x)
    # break
    if len(set(x)) == 5:
        b1 = []
        b2 = []
        for b in x:
            if x.count(b) == 1:
                b1.append(b)
            if x.count(b) == 2:
                b2.append(b)

        if len(b1) == 4 and len(b2) == 2:
            if b2[0] >= (sum(b1) / 4):
                print(count)
                break

