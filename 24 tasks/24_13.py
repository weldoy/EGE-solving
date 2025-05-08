with open('24_13.txt') as f:
    line = f.readline()

minr = 10**10
r = l = k = 0

for r in range(len(line)):
    if line[r] == 'Y':
        k += 1
    while k >= 260:
        minr = min(minr, r-l+1)
        if line[l] == 'Y':
            k -= 1
        l += 1

print(minr)