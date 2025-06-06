import re

f = open('24_6.txt').readline()

pattern = r'S?Q?R?P?(?:SQRP)+(?:S?Q?R?P?)'

res = re.findall(pattern, f)

maxlen = 0
for i in res:
    if len(i) > maxlen:
        maxlen = max(maxlen, len(i))
        print(i)

print(maxlen)
