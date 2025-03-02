from itertools import *

count = 0

words = product('ACGT', repeat=5)

for i in words:
    if i.count('A') == 2:
        count += 1

print(count)
