f = open('9_21976.csv')
k = 0
count = 0
for i in f:
    k += 1
    x = sorted(list(map(int, i.split(','))))
    odds = []
    evens = []
    summaodds = 0
    if len(set(x)) == 4:
        for a in x:
            if a % 2 == 0:
                evens.append(a)
            else:
                odds.append(a)
        for o in odds:
            summaodds += o**3
        if sum(evens) ** 2 > summaodds:
            count += 1
            print(k)

print(count)

