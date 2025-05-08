with open('24_11.txt') as file:
    line = file.readline()

r = l = k = maxr = 0

for r in range(len(line)):
    if line[r] == 'W':
        k += 1
    while k > 130:
        if line[l] == 'W':
            k -= 1
        l += 1
    if k <= 130:
        maxr = max(maxr, r-l+1)

print(maxr)
