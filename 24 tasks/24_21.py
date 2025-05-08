with open('24_21.txt') as f:
    line = f.readline()

k = maxk = 0

for i in range(len(line)):
    if line[i] in '0123456789ABCDEF':
        k += 1
        maxk = max(maxk, k)
    else:
        k = 0

print(maxk)
