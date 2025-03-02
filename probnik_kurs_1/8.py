from itertools import *

count = 0
for p in permutations('иннокентий', r=10):
    count += 1
    print(p, count)
