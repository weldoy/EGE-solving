import re

f = open('24_22360.txt').readline()

pattern = r'[1-9AB][0-9AB]*'

res = re.finditer(pattern, f)

maxs = 0
for i in res:
    if int(i.group(), 12) % 6 == 0:
        maxs = max(maxs, len(i.group()))
        if len(i.group()) == 109:
            print(i)

print(maxs)
