with open('24_6.txt') as f:
    line = f.readline()

r = l = 0
k = 0
maxr = 0

for r in range(len(line) - 1):
    if line[r] == 'W' and line[r-1] == 'W':
        k += 1
    while k > 100:
        if line[l] + line[l+1] == 'WW':
            k -= 1
        l += 1
    if k == 100:
        maxr = max(maxr, r - l + 1)

print(maxr)
