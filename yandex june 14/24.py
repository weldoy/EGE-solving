import re

f = open('24.txt').readline()

pattern = r'E[N | D]+E'

res = re.findall(pattern, f)
maxlen = 0

for i in res:
    if len(i) > maxlen:
        maxlen = len(i)
        print(i)

print(maxlen)
