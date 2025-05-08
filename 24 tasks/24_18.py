with open('24_18.txt') as f:
    line = f.readline()

r = l = maxk = k = 0

for r in range(len(line)):
    if line[r-1] + line[r] == 'AB':
        k += 1
    while k > 21:
        if line[l] + line[l+1] == 'AB':
            k -= 1
        l += 1
    if k == 21:
        maxk = max(maxk, r-l+1)

print(maxk)
