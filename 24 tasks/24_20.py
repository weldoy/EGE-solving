with open('24_20.txt') as f:
    line = f.readline()

r = l = k = 0

mink = 10**10

for r in range(len(line)):
    if line[r] == 'X':
        k += 1
    while k >= 500:
        mink = min(mink, r-l+1)
        if line[l] == 'X':
            k -= 1
        l += 1

print(mink)
