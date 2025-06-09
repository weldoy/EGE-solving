import re

s = '12345123123123213123124313432214412341234234342321341234'

pattern = r'(?:[1][2]*|4)'

res = re.findall(pattern, s)

print(res)
