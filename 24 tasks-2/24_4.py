import re

f = open('24_4.txt').readline()

# f = 'XZYZZYXYYZXZYXXYZX'

r = maxlen = l = 0

while r < len(f) - 1:
    if (f[r] + f[r+1]) not in ('YY', 'XX'):
        r += 1
    else:
        maxlen = max(r - l + 1, maxlen)
        l = r
        while f[l:l+2] in ('XX', 'YY'):
            l += 1
        r = l + 1

print(maxlen)
