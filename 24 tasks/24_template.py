f = open('24_2024.txt').readline()
maxr = 0
k = 0
r = l = 0
for r in range(len(f)):
    if f[r] == 'T':
        k += 1
    while k > 100:
        if f[l] == 'T':
            k -= 1
        l += 1
    if k == 100:
        maxr = max(maxr, r - l + 1)
print(maxr)
