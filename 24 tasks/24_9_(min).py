with open('24_9.txt') as f:
    line = f.readline()

r = l = 0
k = 0
minr = 10**10

for r in range(len(line) - 2):
    if line[r-2] + line[r-1] + line[r] == 'RSQ':
        k += 1
    while k == 130 and line[r] != 'Q':
        minr = min(minr, r-l+1)
        if line[l] + line[l+1] + line[l+2] == 'RSQ':
            k -= 1
        l += 1
print(minr)
