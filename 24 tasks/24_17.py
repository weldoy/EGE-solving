with open('24_17.txt') as f:
    line = f.readline()

r = l = k = 0
minr = 10**10

for r in range(len(line)):
    if line[r-1] + line[r] == 'AB':
        k += 1
    while k == 21:
        minr = min(minr, r-l+1)
        if line[l] + line[l+1] == 'AB':
            k -= 1
        l += 1

print(minr)
