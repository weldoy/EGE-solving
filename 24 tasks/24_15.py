with open('24_15.txt') as f:
    line = f.readline()

r = l = k = 0
minr = 10 ** 10

for r in range(len(line)):
    if line[r] == 'V':
        k += 1
    while k == 999:
        minr = min(minr, r - l + 1)
        if line[l] == 'V':
            k -= 1
        l += 1

print(minr)
