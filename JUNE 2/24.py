import re

# f = open('24_22448.txt').readline()
f = '132B123JEK132K213KK'

pattern = r'[1-9]*'

res = re.findall(pattern, f)
print(res)
