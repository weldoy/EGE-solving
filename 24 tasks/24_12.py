with open('24_12.txt') as f:
    ln = f.readline()

r = l = k = 0
minr = 10**10

for r in range(len(ln)):
    if ln[r] == 'Z':
        k += 1
    while k == 200:
        minr = min(minr, r - l + 1)
        if ln[l] == 'Z':
            k -= 1
        l += 1

print(minr)
