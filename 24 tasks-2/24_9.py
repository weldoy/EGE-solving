import re

f = open('24_20813.txt').readline()

digit = r'(?:[1-9][0-9]*|0)'
pattern = fr'(?:{digit}[-*])*(?:{digit})'

res = re.findall(pattern, f)

print(f'length={len(max(res, key=len))}   {max(res, key=len)}')
