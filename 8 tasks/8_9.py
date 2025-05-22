from itertools import product

count = 0
for i in product('01234567', repeat=5):
    x = ''.join(i)
    if x[0] in '246':
        if x[-1] not in '26':
            if x.count('7') <= 2:
                count += 1

print(count)
