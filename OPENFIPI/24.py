import re

f = open('24_21908.txt').readline()

pattern = r'[1-9A-D][0-9A-D]+'
maxlen = 0
res = re.findall(pattern, f)

for i in res:
    if len(i) > maxlen:
        maxlen = len(i)
        print(i)


print(maxlen)
