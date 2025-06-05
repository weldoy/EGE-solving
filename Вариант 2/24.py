with open('24_22446.txt') as f:
    line = f.readline()

l = maxline = k = 0
r = l + 1

while r < len(line):
    while k < 10000:
        if r == len(line):
            break
        elif line[r:r+3] == 'LND':
            k += 1
        r += 1
        length = r - l + 1
        if length > maxline:
            maxline = length
            print(f'{k=} {length=}')
