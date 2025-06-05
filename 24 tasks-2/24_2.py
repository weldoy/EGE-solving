line = open('8_24.txt').readline()
# line = 'ABADDABADADABDBADAAAB'

left = maxcnt = cnt = right = 0

while right < len(line) - 1:
    a = line[right] + line[right + 1]
    if a in ('AB', 'AD'):
        cnt += 1
        right += 2
    else:
        cnt = 0
        if line[right + 1] == 'A':
            left = right + 1
            right = left
        else:
            while line[right] != 'A':
                right += 1

    maxcnt = max(cnt, maxcnt)

print(maxcnt, len(line))
