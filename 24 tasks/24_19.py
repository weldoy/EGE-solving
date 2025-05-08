with open('24_19.txt') as f:
    line = f.readline()

r = l = maxk = k = 0

for r in range(len(line)):
    if line[r - 1] + line[r] == 'DE':
        k += 1
    while k > 240:
        if line[l] + line[l + 1] == 'DE':
            k -= 1
        l += 1
    if k <= 240:
        maxk = max(maxk, r-l+1)

print(maxk)
