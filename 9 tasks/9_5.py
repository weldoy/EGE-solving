f = open('325_9.csv')

count = 0
for i in f:
    x = sorted(list(map(int, i.split(';'))))
    if (x[3] < (x[0] + x[1] + x[2])) and (len(set(x)) == 4):
        count += 1

print(count)
