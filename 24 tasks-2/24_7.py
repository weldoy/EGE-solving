import re

f = open('24_7.txt').readline()

f = f.replace('4', 'a')
f = f.replace('3', 'e')

pattern = r'(?:yandex)*y?a?n?d?e?x?'

res = re.findall(pattern, f)
maxlen = 0
for i in res:
    if len(i) > maxlen:
        maxlen = max(len(i), maxlen)
        print(i)


print(maxlen)
