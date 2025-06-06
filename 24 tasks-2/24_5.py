import re

f = open('24_5.txt').readline()

pattern = r'[0-9ABCDEF]*[0-9ABCDEF]'

res = re.findall(pattern, f)

maxlen = 0
print(res)
for i in res:
    if len(i) // 6 > maxlen:
        maxlen = max(len(i) // 6, maxlen)

print(maxlen)
