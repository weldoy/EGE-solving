with open('24_7.txt') as f:
    line = f.readline()

r = l = 0
k = 0
maxr = 0

for r in range(len(line)):
    if line[r] == 'Y':
        k += 1
    while k > 150:
        if line[l] == 'Y':
            k -= 1
        l += 1
    if k <= 150:
        maxr = max(maxr, r-l+1)

print(maxr)
