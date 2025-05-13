f = open('9 варианты 1, 2, 3, 4.csv')
cnt = 0
for s in f:
    a=list(map(int,s.split(';')))
    for i in range(len(a)-3):
        if max(a)<(sum(a)-max(a)):
            if ((int(a[i])+int(a[i+1]))==(int(a[i+2])+int(a[i+3]))) or \
                ((int(a[i])+int(a[i+2]))==(int(a[i+1])+int(a[i+3]))) or \
                    ((int(a[i])+int(a[i+3]))==(int(a[i+1])+int(a[i+2]))):
                cnt += 1
print(cnt)