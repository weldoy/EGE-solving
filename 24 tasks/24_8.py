with open('24_8.txt') as f:
    line = f.readline()

r = l = 0
k = 0
maxr = 0
alphabet = 'FSRQ'

for r in range(len(line) - 3):
    if line[r-3] + line[r-2] + line[r-1] + line[r] == alphabet:
        k += 1
    while k > 80:
        if line[l] + line[l+1] + line[l+2] + line[l+3] == alphabet:
            k -= 1
        l += 1
    if k == 80:
        maxr = max(maxr, r-l+1)
        
print(maxr)
