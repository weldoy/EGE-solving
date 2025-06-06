import re

f = open('24_3.txt').readline()

pattern = r'[0-9]*[0-9]'

res = re.findall(pattern, f)

maxlen = 0
for i in res:
    print(i)
    maxlen = max(maxlen, int(i))

print(maxlen)
