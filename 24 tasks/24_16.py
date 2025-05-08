with open('24_16.txt') as f:
    line = f.readline()

r = l = k = maxr = 0

for r in range(len(line)):
    if line[r] == 'A':
        k += 1
    while k > 700:
        if line[l] == 'A':
            k -= 1
        l += 1
    if k <= 700 and line[l:r+1].count('E') == 0:
        maxr = max(maxr, r-l+1)

print(maxr)
