from itertools import *

count = 0
k = 0
for i in product(sorted('ЦИФЕРБЛАТ'), repeat=5):
    x = ''.join(i)
    count += 1
    if x.count('Ф') == x.count('Ц'):
        if count % 2 != 0:
            if x[0] not in 'ИЕА':
                print(count, x)
                k += 1

print(k)
