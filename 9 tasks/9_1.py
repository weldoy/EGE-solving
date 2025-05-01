with open('9_1.csv') as f:
    count = 0
    for i in f:
        x = sorted(list(map(int, i.split(','))))
        if max(x) < x[0] + x[1] + x[2]:
            if len(set(x)) == 3:
                count += 1

print(count)

