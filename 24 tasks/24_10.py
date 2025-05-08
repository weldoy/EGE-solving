with open('24_10.txt') as f:
    line = f.readline()

r = l = 0
k = 0
maxr = 0

for r in range(len(line)):
    if line[r] == 'T':
        k += 1
    while k > 100:
        if line[l] == 'T':
            k -= 1
        l += 1
    if k == 100:
        maxr = max(maxr, r-l+1)

print(maxr)
