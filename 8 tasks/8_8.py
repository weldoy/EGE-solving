from itertools import *

count = 0
for i in product('0123456', repeat=5):
    x = ''.join(i)
    if x[0] != '0' and x[0] in '2468':
        if x[-1] not in '012':
            if x.count('4') <= 1:
                count += 1
                print(x)
print(count)

