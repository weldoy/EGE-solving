f = open('9.csv')

count = 0

for line in f:
    x = sorted(list(map(int, line.split(','))))
    negative = []
    positive = []
    for i in x:
        if i > 0:
            positive.append(i)
        if i < 0:
            negative.append(i)
    if len(negative) >= 1:
        if len(positive) >= 1:
            if len(negative) > len(positive):
                if abs(min(negative)) > max(positive):
                    print(x)
                    count += 1

print(count)
