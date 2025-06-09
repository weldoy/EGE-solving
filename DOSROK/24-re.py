import re

f = open('24.txt').readline()

pattern = r'[1-9AB][0-9AB]+'

res = re.findall(pattern, f)
maxlen = 0
for i in res:
    if int(i, 12) % 2 == 0:
        maxlen = max(maxlen, len(i))

print(maxlen)
