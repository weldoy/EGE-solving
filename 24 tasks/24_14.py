with open('24_14.txt') as f:
    n = f.readline()

r = l = k = maxr = 0

for r in range(len(n)):
    if n[r] == 'X':
        k += 1
    while k > 1000:
        if n[l] == 'X':
            k -= 1
        l += 1
    if k == 1000:
        maxr = max(maxr, r-l+1)

print(maxr)
