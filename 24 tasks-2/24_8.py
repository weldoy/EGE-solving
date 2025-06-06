import re

f = open('24_8.txt').readline()

pattern = r'(?:0|[1-9]\d*)(?:[+*](?:0|[1-9]\d*))*'

res = re.findall(pattern, f)

maxlen = 0
for i in res:
    if eval(i) == 0:
        if len(i) > maxlen:
            maxlen = max(maxlen, len(i))
            print(i)

print(maxlen)
